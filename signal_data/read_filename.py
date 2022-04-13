import numpy as np 
import cv2
from os import listdir
from os.path import isfile, join
from PIL import Image
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy import signal
import serial
import time
import seaborn as sns

#e = np.fromfile(open("C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\filename"), dtype = np.complex64)
#print (e)

def simpleBinRead(filename, numSamps=-1, in_dtype=np.float32, out_dtype=np.complex64, offset=0):
    '''
    Simple, single-file complex data reader. numSamps refers to the number of complex samples.
    '''
    data = np.fromfile(filename, dtype=in_dtype, count=numSamps*2, offset=offset).astype(np.float32).view(out_dtype)
    
    return data

d = simpleBinRead('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\signal_data\\filename09.50.35') #filename16.13.30 nice graph
#peaks, _ = find_peaks(d, height = 0)
counter = 0
total = []
mean_readings = []
abs_power = np.abs(d)
#trash = np.argwhere(np.diff(np.argwhere(abs_power == 0).flatten())) #array of index of all zeros
#print (abs_power[5000000])
#ii = np.argwhere(abs_power!=0)
#ii = np.argwhere(np.diff(ii.flatten()) != 1) #array of index of zeros but within the "on" recording
#new_trash = np.delete(trash, ii)
trash = np.where(abs_power == 0)[0] #indices of all zeros 
ii = np.argwhere(abs_power != 0) #indices of all non_zeros
gap = np.where(np.diff(ii.flatten()) > 10000) #last index of n readings
mean_readings.append(np.mean(abs_power[ii.flatten()[1]:ii.flatten()[gap][0]]))
mean_readings.append(np.mean(abs_power[ii.flatten()[gap][0] + 1:ii.flatten()[-1]]))
num_samps = abs_power.size



# for i in range(num_samps):
#     print (str(i) + " out of " + str(num_samps) + " left")
#     if abs_power[i] > 0.03 or abs_power[i] == 0 and i not in new_trash: 
#         total.append(abs_power[i]) 
#         print ("Current Total Power: " + str(total))
#         if abs_power[i] == 0 and i in new_trash:
#             counter += 1
#             power = np.mean(total)
#             print ("Mean Power " + str(counter) + ": " + str(power)) 
#             mean_readings.append(power)
#             total.clear()     
#new_mean_readings = [x for x in mean_readings if str(x) != 'nan']  
print ("Number of Readings:" + str(len(mean_readings)))  
print (mean_readings)
#mean_readings.extend([0]*474)
#print ("Number of Readings:" + str(len(mean_readings))) 
arr = np.array(mean_readings, dtype = np.float32) 
# print (arr.shape)
# print (arr)
arr = arr.reshape((1,len(mean_readings))).astype('float32')
print (arr)
print (arr.shape)
ax = sns.heatmap(arr, vmin=0, vmax=0.001, annot = True)
plt.show()


# Make into PIL Image and save
# img = Image.fromarray(arr)
# if img.mode != 'RGB':
#     img = img.convert('RGB')
# img.save('new.png')
# img.show()

# pos_power = np.where(abs_power > 0)

# power_db = 10*np.log10(power)
# mean = np.sqrt(np.mean(power**2))
# mean_db = 20*np.log10(mean)

#plt.plot(abs_power)
#plt.plot(peaks, d[peaks], "d")
#plt.show()
#plt.plot(power)
#plt.show()

#plt.plot(pos_power)
#print (d[0:20000000].shape)
#d = d[0:50000000].reshape(5000,10000)
#print (d.shape)
#plt.plot(np.mean(np.abs(d)))
#plt.imshow
#plt.show()



# arduino=serial.Serial('COM3', 9600, timeout = .1)
# time.sleep(2)


# while 1:
#     command = input("Servo Position: ")
#     arduino.write(command.encode())


# Define width and height
#w, h = 50, 100

# Read file using numpy "fromfile()"
#with open('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\signal_data\\filename', mode='rb') as f:
    #d = np.fromfile(f,dtype=np.complex64,count=w*h).reshape(h,w)





#img_rgb = cv2.cvtColor(d, cv2.COLOR_GRAY2BGR)
#print (img_rgb.shape)
#rgb = Image.fromarray(img_rgb)
#rgb.save('rgb.png')