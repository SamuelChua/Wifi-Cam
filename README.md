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
The USRP B205 Mini-i is a SDR designed by Ettus Research which has a Frequency range: 70 MHz – 6 GHz and up to 56 MHz of instantaneous Bandwidth

## Software 
GNURadio 
GNURadio was installed via https://wiki.gnuradio.org/index.php/InstallingGR#For_GNU_Radio_3.10,_3.9,_and_Main_Branch on Windows 

GNU Radio is a free & open-source software development toolkit that provides signal processing blocks to implement software radios. It can be used with readily-available low-cost external RF hardware to create software-defined radios, or without hardware in a simulation-like environment. It is widely used in research, industry, academia, government, and hobbyist environments to support both wireless communications research and real-world radio systems.

Mainly ran using Python 

 ###### Test.py - Gnuradio Companion generated program file to see and listen to different freqs #######
 ###### epy_block_0.py - Python block to link to USRP for timed commands (using time.sleep()) #######
 ###### stream.py - Use Message Strobe + Stream Tags + Custom Py block to rea$d and print tags to freq hop once after 20s ######
 ###### epy_block_0_read_tag.py - Python block to read stream tags ######
