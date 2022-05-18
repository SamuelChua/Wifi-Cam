import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# abs_power = [random.randrange(0,50,1) for i in range(100)]
# total = []
# counter = 0
# mean_readings = []
# num_samps = len(abs_power)
# j = 0
# print (abs_power)


# for i in range(num_samps):
#     if abs_power[i] > 0: #0.001 got 526 readings
#         total.append(abs_power[i]) 
        
#         print ("Current Total Power: " + str(total)) #var total got issues cos originally it was np.mean(one value), next step is to edit it such that it's a list of i items then np.mean

#     elif abs_power[i] == 0:
#         counter += 1
#         power = np.mean(total)
#         print ("Mean Power " + str(counter) + ": " + str(power)) 
#         mean_readings.append(power)
#         total.clear()     
# new_mean_readings = [x for x in mean_readings if str(x) != 'nan']  
# print ("Number of Readings:" + str(len(new_mean_readings)))  
# print (new_mean_readings)


# x = np.array([1,0,9,7,5,23,4,0,1,0])
# for i, val in enumerate(x):
#     print (np.diff(np.where(x==0)))
#     if (val == 0 and np.diff(np.where(x==0)[0]) > 2):
#         print ('hi')
#     else:
#         print ('no')       

command = []


for i in range(0,181,45):
    i = "H:" + str(i)  
    for j in range(0,181,36):
        j = "&V:" + str(j)
        j = i + j
        command.append(j)

print (command)

arduino=serial.Serial('COM3', 9600, timeout = .1)
    #myArduino = serial.mySerial('COM3', 9600)

    time.sleep(2)


    while 1:
        #command = input("Servo Position: ")
        #arduino.write(command.encode())
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
            data = arduino.readline()[:-2]
            time.sleep(5)
        
            if data:
                print (data)    
        # vert = []
        # hori = []
        # for i in range(0,181,45):
        #     i = str(i)
        #     hori.append(i)  

        # for i in hori:
        #     arduino.write(i.encode())
        #     time.sleep(5)

        # for j in range(0,181,36):
        #     j = str(j)
        #     vert.append(j)

        # for i in vert:
        #     myArduino.write(i.encode())
        #     time.sleep(5)    


# vert = []
# hori = []
# for i in range(0,181,45):
#     i = str(i)
#     hori.append(i)  
# for j in range(0,181,36):
#     j = str(j)
#     vert.append(j)
# print (hori)
# print(vert)

# GNU Radio Generated Script with edits from line 257
#Added main_new to set up 'local' GNURadio program to access the switch variable to turn on/off USRP 
def main_new(tb, qapp, options=None):

    # if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
    #     style = gr.prefs().get_string('qtgui', 'style', 'raster')
    #     Qt.QApplication.setGraphicsSystem(style)
    # qapp = Qt.QApplication(sys.argv)

    # tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()

# mean_readings = [0.03920263, 0.038523767, 0.042174436, 0.038397405, 0.038191997, 0.038398925, 0.03216023, 0.038263615, 0.034879856, 0.036539573, 0.03870616, 0.038939357, 0.038662802, 0.038105085, 0.038051296, 0.03855053, 0.042504493, 0.041931894, 0.035576697, 0.035212997, 0.03904309, 0.0354586, 0.031583827, 0.03118855, 0.075962305, 0.073060535, 0.0669021, 0.034266237, 0.06460835, 0.034282535, 0.030957516, 0.0307295, 0.06853102]
# arr = np.array(mean_readings, dtype = np.float32) 
# # print (arr.shape)
# # print (arr)
# arr = arr.reshape((1,33)).astype('float32')
# # print (arr)
# # print (arr.shape)
# ax = sns.heatmap(arr, vmin=0, vmax=0.1, annot = True)
# plt.show()

# def heatmap2d(arr: np.ndarray):
#     plt.imshow(arr, cmap='viridis', vmin = 0, vmax = 0.01)
#     plt.colorbar()
#     plt.show()

# heatmap2d(arr)

# def repeating_key_xor(text: bytes, key: bytes) -> bytes:
#     """Given a plain text `text` as bytes and an encryption key `key`
#     as bytes, the function encrypts the text by performing
#     XOR of all the bytes and the `key` (in repeated manner) and returns
#     the resultant XORed byte stream.
#     """
    
#     # we update the encryption key by repeating it such that it
#     # matches the length of the text to be processed.
#     repetitions = 1 + (len(text) // len(key))
#     key = key * repetitions
#     key = key[:len(text)]

#     # XOR text and key generated above and return the raw bytes
#     return bytes([b ^ k for b, k in zip(text, key)])

# f = open("C:\\Users\\intern\\Downloads\\learn_more_about_CSIT\\secret","rb")
# fr = f.read()
# decrypted = repeating_key_xor(fr, b'CSIT')

# print(decrypted)

# of = open("C:\\Users\\intern\\Downloads\\learn_more_about_CSIT\\new", "wb")
# of.write(decrypted)
# of.close()