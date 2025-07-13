from flask import Flask, render_template, request
import board
import pwmio
from adafruit_motor import motor

left_pwm = pwmio.PWMOut(board.D19, frequency=1000)
right_pwm = pwmio.PWMOut(board.D18, frequency=1000)
left_motor = motor.DCMotor(left_pwm, None)
right_motor = motor.DCMotor(right_pwm, None)
app = Flask(__name__)

def move(l, r):
    left_motor.throttle = l
    right_motor.throttle = r
  
def stop():
    move(0, 0)
  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    data = request.form['key']

    if data == 'w':
        move(1.0, 1.0)
    elif data == 'a':
        move(0.3, 0.8)
    elif data == 'd':
        move(0.8, 0.3)
    elif data == 's':
        move(0.3, 0.3)
    elif data == 'x':
        stop()

    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
