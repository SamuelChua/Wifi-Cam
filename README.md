# Building a 'Wifi-Seeing' Camera

## Description

In this project, I used a software defined radio (SDR) along with a directional Yagi antenna to scan a
cone in front of it and detect Wifi signals, overlaying it on top of a normal camera
image in order to give directional information of signal sources (possibly through
walls!). Overall, I controlled and manipulated both the radio and camera with DSP and arduino control of a servo motor for the antenna. With this application, I'm able to display the spatial awareness of Wifi signals. 

## Table of Contents 
- Hardware/Tools used
- Software
- 


## Hardware/Tools Used
### USRP Software Defined Radio 
The USRP B205 Mini-i is a SDR designed by Ettus Research which has a Frequency range: 70 MHz – 6 GHz and up to 56 MHz of instantaneous Bandwidth


<img src="https://user-images.githubusercontent.com/9492646/168749479-fe65405c-384f-4492-9fda-59c76cafda7e.jpg" width="400">

Yagi Antenna

<img src ="https://user-images.githubusercontent.com/9492646/168747625-059d9247-391d-4e11-9860-cb122a4c1f6c.png" width="400">

https://www.farnell.com/datasheets/1580319.pdf
https://shopee.sg/-2-4GHz-13DBI-15DBI-Yagi-WLAN-WiFi-Wireless-Antenna-for-Router-i.182364102.16345522237

Arduino Servo Motor

https://sg.element14.com/multicomp-pro/mp-708-0001/servo-motor-180deg/dp/3359813?CMP=i-55c5-00001621

## Software 
### GNURadio 
GNU Radio is a free & open-source software development toolkit that provides signal processing blocks to implement software radios. I ran it mainly with Python 

GNURadio was installed via http://www.gcndevelopment.com/gnuradio/downloads.htm on Windows, specifically GNURadio V3.8.2.0-win64 for my project. 




 ###### Test.py - Gnuradio Companion generated program file to see and listen to different freqs #######
 ###### epy_block_0.py - Python block to link to USRP for timed commands (using time.sleep()) #######
 ###### stream.py - Use Message Strobe + Stream Tags + Custom Py block to rea$d and print tags to freq hop once after 20s ######
 ###### epy_block_0_read_tag.py - Python block to read stream tags ######
