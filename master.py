from threading import Thread
import os , multiprocessing
from multiprocessing import Pool, Queue, Event
import time
import serial, queue
# from extract import main
from extract import *
from arduino import arduino
from webcam import webcam
import cv2
#processes = ('extract.py', 'webcam.py', 'arduino.py')

# def read_data(queue_, should_stop):
#     while not should_stop.is_set():
#         # calculate/get cX, cY, angle
#         command = []
#         for i in range(0,181,45):
#             i = "0:" + str(i)  
#             for j in range(0,181,36):
#                 j = "&1:" + str(j)
#                 j = i + j
#                 command.append(j)
#         queue_.put((command))
#         # sleep 30ms

# def send_to_arduino(queue_, should_stop):
#     while not should_stop.is_set():
#         data = queue_.get()
#         command = data
#         arduino=serial.Serial('COM3', 9600, timeout = .1)
#         for i in data:
#             i = str(i)
#             print (i)
#             arduino.write(i.encode())
#             time.sleep(5)
#         #data = arduino.readline()[:-2]
#         #time.sleep(5)
#         # if data:
#         #     print (data)

#         # update ardunio

# def tell_when_to_stop(should_stop):
#     # detect when to stop, and set the Event. For example, we'll wait for 5 seconds and then ask all to stop
#     time.sleep(5)
#     should_stop.set()

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
        time.sleep(5)
        e.set_Switch(1)
        print("gr is on!, %d" % e.Switch)
        time.sleep(5)
        e.set_Switch(0)
        print("gr is off!, %d" % e.Switch)
        #data = arduino.readline()[:-2]

            #if data:
                #print (data)

# def run_process(process):
#     os.system('python {}'.format(process))

def changeSwitch(e):
    # Adjust switch here
    while True: 
        e.set_Switch(1)
        print("gr is on, %d" % e.Switch)
        time.sleep(5)
        
        e.set_Switch(0)
        print("gr is off, %d" % e.Switch)
        time.sleep(5)
        

# def wait_for_event(event):
#     print ("wait_for_event: starting")
#     event.wait()
#     print ("wait_for_event: event.is_set()->", event.is_set())

# def wait_for_event_timeout(event, t):
#     print ("wait_for_event_timeout: starting")
#     event.wait(t)
#     print ("wait_for_event_timeout: event.is_set()->", event.is_set())

# should_stop = Event()

# thread_stop_decider = Thread(target=tell_when_to_stop, args=(should_stop,))
# thread_read = Thread(target=read_data, args=(queue_, should_stop))
# thread_arduino = Thread(target=send_to_arduino, args=(queue_, should_stop))
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



    #event = Event()
    e = extract()
    #condition = multiprocessing.Condition()
    #w1 = multiprocessing.Process(target=wait_for_event, args=(event,))
    #w2 = multiprocessing.Process(target=wait_for_event_timeout, args=(event, 2))
    #ard = multiprocessing.Process(target=arduino, args=(e,))
    web = multiprocessing.Process(target=webcam, args=())
    
    


    
    # Start thread to loop switch
    #thread_switch = Thread(target=changeSwitch, args=(e,))
    thread_test = Thread(target=arduino, args=(e,))

    # w1.start()
    # w2.start()
    # print ('main: waiting before calling Event.set()')
    # time.sleep(3)
    # event.set()
    # print ('main: event is set')
    #ard.start()
    web.start()
    

    #thread_switch.start()
    thread_test.start()
    main_new(e, qapp)

    # End threads
    #thread_switch.join()
    thread_test.join()
    # End processes
    #ard.join()
    web.join()
    # w1.join()
    # w2.join()

    #pool = Pool(processes=3)
    #pool.map(run_process, processes)



    # thread_read.start()
    # thread_arduino.start()
    # thread_stop_decider.start()

    # try:
    #     while thread_read.is_alive():
    #         thread_read.join(1)
    # except KeyboardInterrupt:
    #         should_stop.set()
    # thread_read.join()
    # thread_arduino.join()
    # thread_stop_decider.join()