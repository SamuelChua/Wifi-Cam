from threading import Thread
import os , multiprocessing
from multiprocessing import Pool, Queue, Event
import time
import serial, queue
from extract import *
from arduino import arduino
from webcam import webcam
import cv2

def interval():
    interval.hori_interval = list(range(0,181,45))
    interval.vert_interval = list(range(0,181,36))

def webcam():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")
    start_time = time.time()
    img_counter = 0
    img2_counter = 0
    path = 'C:\\Users\\intern\\Documents\\GitHub\\Wifi-Cam\\image_data\\'

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
        elif time.time() - start_time >= 5: 
        #Check if 5 sec passed
            img2_name = "image_{}.png".format(img2_counter)
            cv2.imwrite(os.path.join(path, img2_name), frame)
            print("{} written!".format(img2_counter))
            start_time = time.time()
            img2_counter += 1

    cam.release()

    cv2.destroyAllWindows()

def arduino(e):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("cam")
    start_time = time.time()
    img_counter = 0
    img2_counter = 0
    path = 'C:\\Users\\intern\\Documents\\GitHub\\Wifi-Cam\\image_data\\'

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("cam", frame)

        k = cv2.waitKey(1)

    arduino=serial.Serial('COM3', 9600, timeout = .1)
    time.sleep(2)
    command = []
    pos_90 = "0:90&1:90" 
    print("90")
    arduino.write(pos_90.encode())
    time.sleep(3)
    print ("Reset...")
    beginpos = "0:0&1:0"
    arduino.write(beginpos.encode())
    time.sleep(10)

    for i in hori_interval:
        i = "0:" + str(i)  
        for j in vert_interval:
            j = "&1:" + str(j)
            j = i + j
            command.append(j)



    for i in command:
        i = str(i)
        print (i)     
        
        #Arduino moves
        arduino.write(i.encode())
        time.sleep(5)

        #GNUradio on and webcam take pic
        e.set_Switch(1)
        print("gr is on!, %d" % e.Switch)
        # img2_name = "image_{}.png".format(img2_counter)
        # cv2.imwrite(os.path.join(path, img2_name), frame)
        # print("{} written!".format(img2_counter))
        # img2_counter += 1
        time.sleep(5)

        #GNUradio off and turn to next angle
        e.set_Switch(0)
        print("gr is off!, %d" % e.Switch)
        #data = arduino.readline()[:-2]

            #if data:
                #print (data)

             
    cam.release()

    cv2.destroyAllWindows()
    
def changeSwitch(e):
    # Adjust switch here
    while True: 
        e.set_Switch(1)
        print("gr is on, %d" % e.Switch)
        time.sleep(5)
        
        e.set_Switch(0)
        print("gr is off, %d" % e.Switch)
        time.sleep(5)
        
if __name__ == '__main__':
    # Run GNURadio locally
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    #Declare Processes and Threads
    e = extract()
    #ard = multiprocessing.Process(target=arduino, args=(e,))
    web = multiprocessing.Process(target=webcam, args=()) #May need to remove
    
    # Start thread to loop switch
    #thread_switch = Thread(target=changeSwitch, args=(e,))

    #Changed Arduino from process to Thread
    thread_ard = Thread(target=arduino, args=(e,)) 
    
    #ard.start()
    web.start()
    #thread_switch.start()
    thread_ard.start()

    main_new(e, qapp)

    # End threads
    #thread_switch.join()
    thread_ard.join()

    # End processes
    #ard.join()
    web.join()

    # TODO: attempt to delete extract object
    
    # Then try to open file
