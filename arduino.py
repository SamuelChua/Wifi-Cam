import serial 
import time

#When Arduino is connected, python program will send list of angles to arduino to turn the antenna 

def arduino():
    arduino=serial.Serial('COM3', 9600, timeout = .1)
    time.sleep(2)
    command = []

    for i in range(0,181,45):
        i = "0:" + str(i)  
        for j in range(0,181,36):
            j = "&1:" + str(j)
            j = i + j
            command.append(j)
    for i in command:
        i = str(i)
        print (i)
        arduino.write(i.encode())
        #data = arduino.readline()[:-2]
        time.sleep(5)

            #if data:
                #print (data)