import numpy as np 
import scipy
from os import listdir
from os.path import isfile, join
from PIL import Image

#e = np.fromfile(open("C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\filename"), dtype = np.complex64)
#print (e)


# Define width and height
w, h = 50, 100

# Read file using numpy "fromfile()"
with open('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\signal_data', mode='rb') as f:
    d = np.fromfile(f,dtype=np.uint8,count=w*h).reshape(h,w)

# Make into PIL Image and save
PILimage = Image.fromarray(d)
PILimage.save('result.png')