import numpy as np 
import scipy
from os import listdir
from os.path import isfile, join

#f = scipy.fromfile(open("C:\Users\intern\Documents\Github\Wifi-Cam\filename"), dtype = scipy.complex64)
f = np.fromfile(open("C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\filename"), dtype = np.complex64)
print (f)