import cv2
import os
images = []
folder = 'C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\image_data\\'
myFolders = [file for file in os.listdir(folder) if file.endswith('.png')]
print (myFolders)


for f in myFolders:
	img = cv2.imread(f'{folder}/{f}')
	#img = cv2.resize(img, (0,0), None, 0.2, 0.2)
	images.append(img)
	stitcher = cv2.Stitcher_create()
	(status,result) = stitcher.stitch(images)
if (status == cv2.STITCHER_OK):
	print ('Panorama Generated...')
	cv2.imshow("pano", result)
	cv2.waitKey(1)
	cv2.imwrite('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\image_data\\pano.png', result)
else: 
	print ('Pano Not Generated')

cv2.waitKey(0)
