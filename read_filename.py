import numpy as np 
import cv2, sys
sys.path.append('C:\\Users\\intern\\Documents\\GitHub\\Wifi-Cam\\master')
from master import interval
from os import listdir
from os.path import isfile, join
from PIL import Image
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy import signal
import serial
import time
import seaborn as sns
import matplotlib.image as mpimg 


#e = np.fromfile(open("C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\filename"), dtype = np.complex64)
#print (e)

def simpleBinRead(filename, numSamps=-1, in_dtype=np.float32, out_dtype=np.complex64, offset=0):
    '''
    Simple, single-file complex data reader. numSamps refers to the number of complex samples.
    '''
    data = np.fromfile(filename, dtype=in_dtype, count=numSamps*2, offset=offset).astype(np.float32).view(out_dtype)
    
    return data

d = simpleBinRead('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\signal_data\\filename15.46.11') #filename16.13.30 nice graph
#peaks, _ = find_peaks(d, height = 0)

mean_readings = []
abs_power = np.abs(d)
#trash = np.argwhere(np.diff(np.argwhere(abs_power == 0).flatten())) #array of index of all zeros
#ii = np.argwhere(np.diff(ii.flatten()) != 1) #array of index of zeros but within the "on" recording
trash = np.argwhere(abs_power == 0) #indices of all zeros 
ii = np.argwhere(abs_power != 0) #indices of all non_zeros
gap = np.where(np.diff(ii.flatten()) > 10000) #last index of n-1 readings recorded
#index = [0, -1]
#new_gap = np.delete(gap, index)
#print (new_gap) 
gap1 = gap[0][:-1]
print (gap1)

#calculate mean reading for specfic horizontal and vertical angle (eg 30degree H and 30degrees V)
mean_readings.append(np.mean(abs_power[ii.flatten()[1]:ii.flatten()[gap[0][0]]])) #first reading
for i, elem in enumerate(gap1):  

    if elem == gap1[-1]: #2nd last reading
        mean_readings.append(np.mean(abs_power[ii.flatten()[elem+1]:ii.flatten()[gap[0][-1]]])) #2nd last reading
        break
    else:
        mean_readings.append(np.mean(abs_power[ii.flatten()[elem+1]:ii.flatten()[gap1[i+1]]]))           

mean_readings.append(np.mean(abs_power[ii.flatten()[gap[0][-1] + 1]:ii.flatten()[-1]])) #last reading






print ("Number of Readings:" + str(len(mean_readings)))  #all vertical/horizontal readings in one list 
print (mean_readings)
arr = np.array(mean_readings, dtype = np.float32) 

interval()
num_vert = len(interval.vert_interval) #number of vertical readings taken
print (num_vert)
num_hori = int(len(mean_readings)/num_vert)

# arr = arr.reshape((num_vert, num_hori)).astype('float32') #need to double check how all the readings are changed in terms of order 
arr = arr.reshape((num_hori, num_vert)).T
arr = arr[np.arange(5,-1,-1),:]
print (arr)
print (arr.shape)
x_axis_labels = interval.hori_interval # labels for x-axis
y_axis_labels = np.flip(interval.vert_interval) # labels for y-axis
ax = sns.heatmap(arr, annot = True, alpha = 0.5, zorder = 2, xticklabels=x_axis_labels, yticklabels=y_axis_labels)
ax.set(xlabel="Horizontal Angle", ylabel="Vertical Angle")
my_img = mpimg.imread("C:\\Users\\intern\\Downloads\\DSO.jpg")
ax.imshow(my_img, aspect=ax.get_aspect(), extent=ax.get_xlim() + ax.get_ylim(), zorder=1)
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