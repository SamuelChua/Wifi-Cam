import numpy as np 
import cv2
from os import listdir
from os.path import isfile, join
from PIL import Image
import matplotlib.pyplot as plt

#e = np.fromfile(open("C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\filename"), dtype = np.complex64)
#print (e)

def simpleBinRead(filename, numSamps=-1, in_dtype=np.float32, out_dtype=np.complex64, offset=0):
    '''
    Simple, single-file complex data reader. numSamps refers to the number of complex samples.
    '''
    data = np.fromfile(filename, dtype=in_dtype, count=numSamps*2, offset=offset).astype(np.float32).view(out_dtype)
    
    return data

d = simpleBinRead('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\signal_data\\filename11.02.01') #filename16.13.30 nice graph
print (d[0:20000000].shape)
#d = d[0:50000000].reshape(5000,10000)
print (d.shape)
plt.plot(np.abs(d))
#plt.imshow
plt.show()

# Define width and height
#w, h = 50, 100

# Read file using numpy "fromfile()"
#with open('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\signal_data\\filename', mode='rb') as f:
    #d = np.fromfile(f,dtype=np.complex64,count=w*h).reshape(h,w)



# Make into PIL Image and save
#PILimage = Image.fromarray(d)
#print (d.shape)
#PILimage.save('result.png')

#img_rgb = cv2.cvtColor(d, cv2.COLOR_GRAY2BGR)
#print (img_rgb.shape)
#rgb = Image.fromarray(img_rgb)
#rgb.save('rgb.png')