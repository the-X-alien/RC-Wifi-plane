from flask import Flask, render_template_string, request, Response
import RPi.GPIO as GPIO
from picamera2 import Picamera2
import cv2

app = Flask(__name__)

# GPIO Setup
LEFT_PIN = 13
RIGHT_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEFT_PIN, GPIO.OUT)
GPIO.setup(RIGHT_PIN, GPIO.OUT)

pwm_left = GPIO.PWM(LEFT_PIN, 100)
pwm_right = GPIO.PWM(RIGHT_PIN, 100)
pwm_left.start(0)
pwm_right.start(0)

plane_on = False

def set_motor(left, right):
    pwm_left.ChangeDutyCycle(left)
    pwm_right.ChangeDutyCycle(right)

# Picamera2 setup
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue  # skip frame if encoding fails
        jpg_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n')

@app.route('/stream.mjpg')
def stream():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/', methods=['GET', 'POST'])
def index():
    global plane_on
    if request.method == 'POST':
        key = request.form['key']
        if key == 'x':
            plane_on = not plane_on
            if not plane_on:
                set_motor(0, 0)
        elif plane_on:
            if key == 'w':
                set_motor(80, 80)
            elif key == 's':
                set_motor(0, 0)
            elif key == 'a':
                set_motor(40, 80)
            elif key == 'd':
                set_motor(80, 40)
    return render_template_string(TEMPLATE)

@app.route('/shutdown')
def shutdown():
    set_motor(0, 0)
    pwm_left.stop()
    pwm_right.stop()
    GPIO.cleanup()
    return "Shutdown complete."

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Control Panel</title>
    <style>
        body {
            background: #0f172a;
            color: #f8fafc;
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 2rem;
        }
        h1 {
            color: #38bdf8;
            margin-bottom: 1rem;
        }
        form {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            justify-content: center;
            margin-bottom: 2rem;
        }
        button {
            padding: 1rem 2rem;
            font-size: 1.25rem;
            border: none;
            border-radius: 10px;
            background-color: #1e293b;
            color: #f1f5f9;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }
        button:hover {
            background-color: #38bdf8;
            color: #0f172a;
        }
        .stream {
            border: 4px solid #38bdf8;
            border-radius: 10px;
            margin-bottom: 1.5rem;
        }
        footer {
            color: #94a3b8;
            font-size: 1rem;
            margin-top: auto;
        }
    </style>
    <script>
        document.addEventListener("keydown", function(event) {
            const keys = ['w', 'a', 's', 'd', 'x'];
            if (keys.includes(event.key.toLowerCase())) {
                fetch("/", {
                    method: "POST",
                    headers: {"Content-Type": "application/x-www-form-urlencoded"},
                    body: "key=" + event.key.toLowerCase()
                });
            }
        });
    </script>
</head>
<body>
    <h1>Control Panel</h1>
    <img class="stream" src="/stream.mjpg" width="640" height="480" alt="Live Camera Feed">
    <form method="POST">
        <button name="key" value="w">W</button>
        <button name="key" value="a">A</button>
        <button name="key" value="s">S</button>
        <button name="key" value="d">D</button>
        <button name="key" value="x">Toggle</button>
    </form>
    <footer>With &lt;3 by Dhiaan, Jake, and Alfonso</footer>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
