# The RC plane over wifi, connect from anywhere on the network
Youtube Video: https://youtu.be/5Vv8Iro-fa4
---
<img width="851" height="429" alt="image" src="https://github.com/user-attachments/assets/7264e9a8-5da0-426a-8ac3-8a4115cee9ee" />

---
all the hardware is positioned under the plane and we haven't attached the propellers

---
We wanted to create a interactive robot that was fun to use, even if you aren't the one behind the controls. After thinking about robots like a balcning robot or car we thoguht about a flying car. we realied though that a flying car wouldn't work since we didn't have nearly powerfull enough motors, nor the hardware to create a drone. Then I started thinking about planes. They fly like a drone, but get this, they glide-bet you didn't know that. because of the lfit generated by the wings planes can be a lot more stable with less tuning(or at least thats what we hoped). We didn't have any powerfull motors though so we bought some- by scrapping a 25 dollar drone from Best Buy. 
<img width="773" height="522" alt="Screen Shot 2025-07-13 at 10 27 09 AM" src="https://github.com/user-attachments/assets/f6ed6022-da57-44f7-b53b-18c1c765aa46" />
## The electronics
using a Rpi zero 2 w, since it can stream a camera feed and has a ton of GPIO's. we powered the whole thing off of a 9 volt with a buck converter to step it down to 5v.
![electronics](https://github.com/user-attachments/assets/14569d53-4086-4aeb-95bd-1a9f6b5ead1b)
## Control!
we ran a webserver powered by flask written by Dhiaan, with Alfonso assiting Dhiaan with learning how to round corners and other CSS stuff. It's pretty minimalistic, with a box for the video stream and buttons for controlling the motors
## Range
This thing can connect anywhere in Github HQ beacause it's range is the range of the Wifi.
## Challenges
We started off with many and we then narrowed them down. Our first version consisted of 3 planes and wasn't wireless so we were gonna find a radio module for that but we couldn't find one. Then we learned that Jake had Xiao ESP32 C6s however we were orginally planning for alot more metrics shown on our web server. So we decided for an I2C Master and Slave to utilize the analog GPIO pins of the Orpheus Picos. Then we reaised that their motors aren't meant for flying and they have low RPM. However, John, the guy stationing the hardware bar at the time told us to take of the gear box. So we took it off but it wasn't fast enough. So then on Saturday we got a 20 dollar bill each to buy food outside of our choice and we made a super smart move. We took the pooled amount as $60 and decided we would buy a large pizza from dominos and then a pre built drone to scrap for parts. 
<img width="1280" height="460" alt="plane render" src="https://github.com/user-attachments/assets/df31075a-ea26-43f6-8ccd-5dabcc1f5362" />

So we bought a $25 dollar drone and scrapped it. We realised that the tiny module isn't powerful enough for this so we got a Raspberry Pi Zero 2 W and we ran a whole web server on it. However Raspberry Pi foundation doesn't have packages for their cameras anymore and they basically don't work. Lucikliy after so many linux commands and so much effort, we finally found a very small unknown inbuilt module that is legacy called Picamera 2. We finally got the livestream working and we realised that we can literally stream the Camera from the roof with no lag. Finaly now after reading so many docs on PWM and how to stear, we finally have working buttons, so now we are just gonna solder everything and run the final thing. After shipping I hope to sleep beacause we pulled an all-nighter. So we'll sleep untill shipping ends beacause then they will start cermonies and stuff so untill then I (Dhiaan) will sleep atleast.

<img width="900" height="875" alt="image" src="https://github.com/user-attachments/assets/c712b3fa-9111-4cbc-b217-33b4fcd323b9" />

## Future Updates and Support
Our plans for the future are to implement an Auto Pilot system that doesnt really fly the drone but just helps it avoid obstacles. So we'll use IR sensors and set minimum distances and then to move back when they are reached. Then we also realzied that our drone will only work indoors where there is wifi which it can hook up on. So prehaps in the future we make it like a bluetooth device or to keep the UI Alfonso and I (Dhiaan) built with so much effort we will just make the Zero run it's own network so we can connect to the network and then fly outdoors. We will probably think of more ideas in the future but this is it for now.
---
##Wiring Diagram 
![wiring_diagram](https://github.com/user-attachments/assets/cf51d3e2-b516-4330-8115-2f6a21da13ca)
         


## Pls vote and follow us for more cool projects that you'll actaully wanna check out and you follow us so you don't have to search for the cool projects and stuff.
---
