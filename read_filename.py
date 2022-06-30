import numpy as np 
import cv2, sys
sys.path.append('C:\\Users\\intern\\Documents\\GitHub\\Wifi-Cam\\master')
from master import interval
from os import listdir
from os.path import isfile, join
import os
from PIL import Image
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy import signal
import serial
import time
import seaborn as sns
import matplotlib.image as mpimg 

def simpleBinRead(filename, numSamps=-1, in_dtype=np.float32, out_dtype=np.complex64, offset=0):
    '''
    Simple, single-file complex data reader. numSamps refers to the number of complex samples.
    '''
    data = np.fromfile(filename, dtype=in_dtype, count=numSamps*2, offset=offset).astype(np.float32).view(out_dtype)
    
    return data

d = simpleBinRead('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\signal_data\\filename16.51.43') #filename16.13.30 nice graph

mean_readings = [] #Creating a list to store mean power readings
abs_power = np.abs(d) #Calculating absolute power 

trash = np.argwhere(abs_power == 0) #indices of all zeros 
ii = np.argwhere(abs_power != 0) #indices of all non_zeros
gap = np.where(np.diff(ii.flatten()) > 10000) #out of all the non_zero data, returns the last index of every reading except the last reading
gap1 = gap[0][:-1] #Remove last element from gap
print (gap1) 

#calculate mean readings for specfic horizontal and vertical angle (eg 30degree Hori and 30degrees Vert)

mean_readings.append(np.mean(abs_power[ii.flatten()[0]:ii.flatten()[gap[0][0]]])) #calculate mean of first reading
#ii.flatten()[gap[0][0]] gives last index of first reading

for i, elem in enumerate(gap1):  
    if elem == gap1[-1]: #2nd last reading of all the readings
        mean_readings.append(np.mean(abs_power[ii.flatten()[elem+1]:ii.flatten()[gap[0][-1]]])) #ii.flatten()[elem] returns last index of 3rd last reading and +1 will return the first index of 2nd last reading. ii.flatten()[gap[0][-1]] returns last index of 2nd last reading
        break
    else:
        mean_readings.append(np.mean(abs_power[ii.flatten()[elem+1]:ii.flatten()[gap1[i+1]]])) #ii.flatten()[elem] returns last index of xth reading and +1 will return the first index of (x+1)th reading. ii.flatten()[gap1[i]] returns the index of the current reading in gap1 then +1 will return the index of the next reading in gap1 which are indices for abs_power

mean_readings.append(np.mean(abs_power[ii.flatten()[gap[0][-1] + 1]:ii.flatten()[-1]])) #last reading: ii.flatten()[gap[0][-1]] returns last index of 2nd last reading and the +1 will return first index of last reading, ii.flatten()[-1] returns last non-zero index

print ("Number of Readings:" + str(len(mean_readings)))  #all vertical/horizontal readings in one list 
print (mean_readings)
arr = np.array(mean_readings, dtype = np.float32) #convert list to np.array


#Cropping Image
num = 0
folder = 'C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\image_data\\'

myFolders = [file for file in os.listdir(folder) if file.endswith('.png')]
myFolders.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

for f in myFolders:
  path1 = os.path.join(folder,f)
  im = Image.open(path1)
  im_crop = im.crop((0, 0, 380, 480)) 
  #im_crop = im.crop((210,0,380,320)) #center crop 
  crop_dir = folder + '\\' + 'cropped' + '\\' + str(num) + '_cropped' + '.png'
  im_crop.save(crop_dir, quality=95)
  num += 1

interval()
num_vert = len(interval.vert_interval) #number of vertical readings taken
print (num_vert)
num_hori = int(len(mean_readings)/num_vert)

# arr = arr.reshape((num_vert, num_hori)).astype('float32') #need to double check how all the readings are changed in terms of order 
arr = arr.reshape((num_hori, num_vert)).T
arr = arr[np.arange(5,-1,-1),:] #rearrange 2d array to desired format for picture display
print (arr)
print (arr.shape)
x_axis_labels = interval.hori_interval # labels for x-axis
y_axis_labels = np.flip(interval.vert_interval) # labels for y-axis

# Plot image + heatmap
ax = sns.heatmap(arr, annot = True, alpha = 0.5, zorder = 2, xticklabels=x_axis_labels, yticklabels=y_axis_labels)
ax.set(xlabel="Horizontal Angle", ylabel="Vertical Angle")


vert_list = list(range(0,num_vert+1))
hori_list = list(range(0,num_hori+1))
reversed_vert_list = reversed(vert_list)

#ax.imshow(my_img, aspect=ax.get_aspect(), extent=ax.get_xlim() + ax.get_ylim(), zorder=1)

myFolders = [file for file in os.listdir(os.path.join(folder,'standby')) if file.endswith('.png')]
myFolders.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
print (myFolders)


index = num_vert
index1 = num_vert
index2 = num_vert
index3 = num_vert
index4 = num_vert

def vindex_iter():
    v_index = iter(reversed_vert_list)
    for i in v_index:
        v = i
        print (v)
        break
    return v
def hindex_iter(): 
    h_index = iter(hori_list)
    h = next(h_index)
    print (h)
    return h
#Iter got issues 
vindex_iter()
hindex_iter()
vindex_iter()
hindex_iter()
vindex_iter()
hindex_iter()
vindex_iter()
hindex_iter()

# TODO change 1,2,3,4,5 to hori_list
for i in range(len(myFolders)):
    img = os.path.join(r'C:\Users\intern\Documents\GitHub\Wifi-Cam\image_data\cropped', myFolders[i])
    if i < num_vert:
        my_img = mpimg.imread(img)
        ax.imshow(my_img, aspect=ax.get_aspect(), extent=(0,1,vert_list[index],vert_list[index-1]), zorder=1)
        index -= 1
    elif i < 2*num_vert:
        my_img = mpimg.imread(img)
        ax.imshow(my_img, aspect=ax.get_aspect(), extent=(1,2,vert_list[index1],vert_list[index1-1]), zorder=1)
        index1 -= 1
    elif i < 3*num_vert:
        my_img = mpimg.imread(img)
        ax.imshow(my_img, aspect=ax.get_aspect(), extent=(2,3,vert_list[index2],vert_list[index2-1]), zorder=1)
        index2 -= 1
    elif i < 4*num_vert:
        my_img = mpimg.imread(img)
        ax.imshow(my_img, aspect=ax.get_aspect(), extent=(3,4,vert_list[index3],vert_list[index3-1]), zorder=1)
        index3 -= 1
    elif i < 5*num_vert:
        my_img = mpimg.imread(img)
        ax.imshow(my_img, aspect=ax.get_aspect(), extent=(4,5,vert_list[index4],vert_list[index4-1]), zorder=1)
        index4 -= 1
    else:
        pass
plt.show()

