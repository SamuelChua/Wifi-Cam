import cv2
import time
import os

#Once webcam is opened, we can wait for 5s to take an image, press SPACE to take an image or press ESC to quit the programme

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