import cv2
import numpy as np


# method 1 ：using cv2.cvtColor(sourceImage,cv2.COLOR_BGR2GRAY)
bgr_img=cv2.imread("imori.jpg")
gray_img=cv2.cvtColor(bgr_img,cv2.COLOR_BGR2GRAY)


#method 2: split the dim
b=bgr_img[:,:,0]
g=bgr_img[:,:,1]
r=bgr_img[:,:,2]
gray_img=(b*0.0722+g*0.7152+0.2126 * r).astype(np.uint8)


cv2.imshow("gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()