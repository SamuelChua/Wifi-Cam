# Building a 'Wifi-Seeing' Camera

## Description

In this project, I used a software defined radio (SDR) along with a directional Yagi antenna to scan and detect Wifi signals, overlaying it on top of a normal camera
image in order to give directional information of signal sources (possibly through
walls!). Overall, I controlled and manipulated both the radio and camera with DSP and arduino control of a servo motor for the antenna. With this application, I'm able to display the spatial awareness of Wifi signals. 

![WhatsApp Image 2022-06-30 at 9 37 27 AM (1)](https://user-images.githubusercontent.com/9492646/176574401-93061b6d-65b6-4043-aba7-005dd80cb512.jpeg)


## Table of Contents 
- Hardware/Software Tools used
- Programs/Files
- Running the program
- Video Demonstration
- Ideas I experimented with along the way
- Concluding Remarks 


## Hardware/Software Tools Used
### USRP Software Defined Radio 
The USRP B205 Mini-i is a SDR designed by Ettus Research which has a Frequency range: 70 MHz – 6 GHz and up to 56 MHz of instantaneous Bandwidth. Using SDR technologies can allow me to easily configure to the requirements I'm looking to detect Wifi signals
<img src="https://user-images.githubusercontent.com/9492646/168749479-fe65405c-384f-4492-9fda-59c76cafda7e.jpg" width="400">

### Yagi Antenna
The 2.4GHz Yagi Antenna is a directional antenna which has a good front-to-back ratio of 16dB to minimise unwanted signals. 
<img src ="https://user-images.githubusercontent.com/9492646/168747625-059d9247-391d-4e11-9860-cb122a4c1f6c.png" width="400">

Here are some links to the datasheet of the antenna 

https://www.farnell.com/datasheets/1580319.pdf

### Servo Motor
Despite its small size, the servo motor has a peak stall torque of 1.5kg.cm which is sufficient to rotate the antenna (300g) given certain support of the antenna. Similarly, here are some links to the datasheet of the servo motor

https://sg.element14.com/multicomp-pro/mp-708-0001/servo-motor-180deg/dp/3359813?CMP=i-55c5-00001621
https://www.farnell.com/datasheets/2914226.pdf


### GNURadio 
GNU Radio is a free & open-source software development toolkit that provides signal processing blocks to implement software radios. I ran it mainly with Python 

GNURadio was installed via http://www.gcndevelopment.com/gnuradio/downloads.htm on Windows, specifically GNURadio V3.8.2.0-win64 for my project. 

### Arduino
Arduino is an open-source tool for electronics projects which consists of the microcontroller and an IDE to run and upload code to the physical Arduino code. 

### Reimage Package

Credits to my mentor, Gabriel. I can save the trouble of repeatedly running np.abs(d) and the lag to generate a graph
https://github.com/icyveins7/reimage

## Programs/Files
Webcam
- Controlling the USB Webcam

Arduino
- Will send Arduino list of angles via serial communication from Python to Arduino

Master
- Master Program to control the GNURadio, Arduino and Webcam 

Extract
- GNURadio generated script with additional new_main function to access GNURadio 'locally'

Pano
- Generate panorama from the photos taken by webcam

Read_filename
- Data processing of bin file generated from GNURadio to give final heatmap of relative power from Wifi signals + overlaying picture of surrounding

Vert_Hori
- Arduino code to accept the list of angles from Arduino.py, and move the servos to control the vertical and horizontal movement of the antenna via serial communication between Python and Arduino

Sweep/Servo Motor
- Arduino test code to ensure that the servo is working 

Reimage package
- To visualise recorded RF data in IQ samples

3D Prints
- STL and SCAD files for 3D printing
- Infill Density 30-50% depending on application (how dense is the print)
- Made use of MakerBot.Print/GrabCAD Print (Using UPrint SE Plus/Industry Printer in DSO Playground of which those with PRINT extension used GrabCAD Print)

## Running the program
After installing GNURadio, ensure the connnections are made between the servo and Arduino and USRP is plugged into your device. Run master.py in GNURadio command line with the extract.py in the same directory and let the fun begin! 

![Screenshot 2022-05-18 095213](https://user-images.githubusercontent.com/9492646/168941075-4526fc6e-8b72-4cc3-b572-3a572cb08138.png)

### GNURadio Flowgraph

There are 2 routes you can use the flowchart

1. Muting the signal via a "Switch" (Used in this project)
By making use GT GUI Chooser with my Multiply Const block, I can change the value of the constant in the GNURadio interacing when running the script, just muting the USRP source by a flick of a switch. 

![Screenshot 2022-05-17 165110](https://user-images.githubusercontent.com/9492646/168771117-054ba7d7-ef64-4d49-b680-3421b9b1d986.png)

2. Timed Intervals 
Created a custom embedded python block to record for n seconds then mute the USRP signal for n seconds. The cycle will then continue

![Screenshot 2022-05-17 165326](https://user-images.githubusercontent.com/9492646/168771553-8c1bdca7-b0c1-4f9e-bae3-426936dc4b34.png)


### Arduino (Vert_Hori)

The code is designed to split the string of angles arduino.py sends into its horizontal & vertical components and having map the speed to control the movement of the servo 

### read_filename

Below is the illustration of how the mean power values are calculated 
![Screenshot 2022-05-19 113415 png-mh](https://user-images.githubusercontent.com/9492646/169213792-75017b86-2e38-4fe8-897f-c362347d715e.png)


## Video Demonstration

Refer to https://youtu.be/VoVrBwUprhU

## Ideas I experimented with along the way: 

### GNURadio
#### Generating the output bin file:
- Using a selector block and n file sinks as output (Able to get 6 separate readings in 6 bin files but limitation was the version I was using couldn't update to latest selector block with input and output index to swap between different output indices. Additionally, having n sinks to give n separate readings wouldn't be sustainable to keep adding file sink blocks in GNURadio)

![Screenshot 2022-05-17 170300](https://user-images.githubusercontent.com/9492646/168773626-3483b6c3-6ccc-4434-85a8-b717e60b41ca.png)


- Using custom python blocks to swap sinks (Swap File Sink & Custom File Sink)
Couldn't come to fruition, nonetheless might need more than 1 file sink as it may not be possible to reuse the same file sink after swapping to null sink
Note that Custom File Sink is a Hier Block

![Screenshot 2022-05-17 165818](https://user-images.githubusercontent.com/9492646/168772523-772d2026-9a67-4c41-b95b-c8be478d2ec5.png)
![Screenshot 2022-05-17 171704](https://user-images.githubusercontent.com/9492646/168776395-debf46ec-f20b-4bac-83bc-ea0077672ce4.png)

- Getting the GNURadio to record the data using stream tags (stream.grc/tagged file sink.grc). Had trouble to generate tags and getting the flowchart to recognise these tags/bursts to switch the on/off record 

- Getting timed recordings using the 'head' block in GNURadio(extract_nogui.grc). It did work to an extent, as it will turn off the USRP afterwards and not knowing how it can turn on again

## Concluding Remarks 
I thoroughly enjoyed the entire process of figuring out how open source frameworks like GNURadio and Arduino work, building my own 'WiFi-seeing' camera from scratch independently. I'm most certainly looking forward to exploiting more technologies that touch both hardware and software. Feel free to reach out for any questions! 

