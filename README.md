# Building a 'Wifi-Seeing' Camera

## Description

In this project, I used a software defined radio (SDR) along with a directional Yagi antenna to scan a
cone in front of it and detect Wifi signals, overlaying it on top of a normal camera
image in order to give directional information of signal sources (possibly through
walls!). Overall, I controlled and manipulated both the radio and camera with DSP and arduino control of a servo motor for the antenna. With this application, I'm able to display the spatial awareness of Wifi signals. 

*Insert Picture of Full Set-Up*

## Table of Contents 
- Hardware/Tools used
- Software
- Python Programs


## Hardware/Software Tools Used
### USRP Software Defined Radio 
The USRP B205 Mini-i is a SDR designed by Ettus Research which has a Frequency range: 70 MHz – 6 GHz and up to 56 MHz of instantaneous Bandwidth


<img src="https://user-images.githubusercontent.com/9492646/168749479-fe65405c-384f-4492-9fda-59c76cafda7e.jpg" width="400">

Yagi Antenna

<img src ="https://user-images.githubusercontent.com/9492646/168747625-059d9247-391d-4e11-9860-cb122a4c1f6c.png" width="400">

https://www.farnell.com/datasheets/1580319.pdf
https://shopee.sg/-2-4GHz-13DBI-15DBI-Yagi-WLAN-WiFi-Wireless-Antenna-for-Router-i.182364102.16345522237

Servo Motor

https://sg.element14.com/multicomp-pro/mp-708-0001/servo-motor-180deg/dp/3359813?CMP=i-55c5-00001621


### GNURadio 
GNU Radio is a free & open-source software development toolkit that provides signal processing blocks to implement software radios. I ran it mainly with Python 

GNURadio was installed via http://www.gcndevelopment.com/gnuradio/downloads.htm on Windows, specifically GNURadio V3.8.2.0-win64 for my project. 

Arduino is also an open-source tool for electronics projects which consists of the microcontroller and an IDE to run and upload code to the physical Arduino code

### Reimage Package

Credits to my mentor, Gabriel https://github.com/icyveins7/reimage

## Python Programs 

GNURadio Flowgraph

There are 2 routes you can use the flowchart

1. Muting the signal via a "Switch" (Used in this project)
By making use GT GUI Chooser with my Multiply Const block, I can change the value of the constant in the GNURadio interacing when running the script, just muting the USRP source by a flick of a switch. 

![Screenshot 2022-05-17 165110](https://user-images.githubusercontent.com/9492646/168771117-054ba7d7-ef64-4d49-b680-3421b9b1d986.png)



2. Timed Intervals 

![Screenshot 2022-05-17 165326](https://user-images.githubusercontent.com/9492646/168771553-8c1bdca7-b0c1-4f9e-bae3-426936dc4b34.png)



Other ways that I attempted: 
Using a selector block and n file sinks as output (Able to get 6 separate readings in 6 bin files but limitation was the version I was using couldn't update to latest selector block with input and output index to swap between different output indices. Additionally, having n sinks to give n separate readings wouldn't be sustainable to keep adding file sink blocks in GNURadio)

![Screenshot 2022-05-17 170300](https://user-images.githubusercontent.com/9492646/168773626-3483b6c3-6ccc-4434-85a8-b717e60b41ca.png)


Using custom python blocks to swap sinks (Swap File Sink & Custom File Sinks)
Couldn't come to fruition 


![Screenshot 2022-05-17 165818](https://user-images.githubusercontent.com/9492646/168772523-772d2026-9a67-4c41-b95b-c8be478d2ec5.png)






Webcam
Arduino
Master


Extract

Read_filename
Pano


Run from master

 ###### Test.py - Gnuradio Companion generated program file to see and listen to different freqs #######
 ###### epy_block_0.py - Python block to link to USRP for timed commands (using time.sleep()) #######
 ###### stream.py - Use Message Strobe + Stream Tags + Custom Py block to read and print tags to freq hop once after 20s ######
 ###### epy_block_0_read_tag.py - Python block to read stream tags ######
