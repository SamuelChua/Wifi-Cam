import cv2
import os
from master import interval
from PIL import Image
images = []
pano_images = []
num = 0
folder = 'C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\image_data\\'
folder_ = 'C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\image_data\\cropped'

#NOT IN USE BECAUSE PANO GENERATED ABIT WEIRD

myFolders = [file for file in os.listdir(folder) if file.endswith('.png')]
myFolders.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

# for f in myFolders:
# 	path1 = os.path.join(folder,f)
# 	im = Image.open(path1)
# 	im_crop = im.crop((0, 0, 380, 480))
# 	crop_dir = folder + '\\' + 'cropped' + '\\' + str(num) + '_cropped' + '.png'
# 	im_crop.save(crop_dir, quality=95)
# 	num += 1

interval()
num_vert = len(interval.vert_interval) #number of vertical readings taken
#num_hori = int(len(mean_readings)/num_vert) #number of horizontal readings taken
num = 0

myFolders = [file for file in os.listdir(os.path.join(folder,'cropped')) if file.endswith('.png')]
myFolders.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
print (myFolders)

for i,f in enumerate(os.listdir('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\image_data\\cropped')):
	# if i < num_vert:
	# 	images.append(myFolders[i])
	# 	images.append(myFolders[i+num_vert*(i%num_vert==0)])
	# 	print (len(images))
	# 	print (images)
	img = cv2.imread(f'{folder_}/{f}')
	images.append(img)
	stitcher = cv2.Stitcher_create()
	(status,result) = stitcher.stitch(images)
	if (status == cv2.STITCHER_OK):
		print ('Panorama Generated...')
		cv2.imshow("pano", result)
		cv2.waitKey(1)
		workdir = folder + '\\' + 'pano_gen' + '\\' + '0' + '.png'
		cv2.imwrite(workdir, result)
		num += 1
		images = []
	else: 
		print ('Pano Not Generated')
		
	# else:
	# 	pass
		# img = cv2.imread(f'{folder}/{f}')
		# images.append(img)

	
for f in os.listdir('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\image_data\\pano_gen'):
	img = cv2.imread(f'{folder}/{f}')
	#img = cv2.resize(img, (0,0), None, 0.2, 0.2)
	pano_images.append(img)
	stitcher = cv2.Stitcher_create()
	(status,result) = stitcher.stitch(pano_images)
	if (status == cv2.STITCHER_OK):
		print ('Final Panorama Generated...')
		cv2.imshow("pano", result)
		cv2.waitKey(1)
		cv2.imwrite('C:\\Users\\intern\\Documents\\Github\\Wifi-Cam\\image_data\\final_pano.png', result)
	else: 
		print ('Final Pano Not Generated')

#cv2.waitKey(0)
