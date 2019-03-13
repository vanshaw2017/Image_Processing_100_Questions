import cv2
import numpy as np

# Inorder to make a binarization ,you need to first change the RGB image to gray.(refer to Q2)
# secondly,notify a threshold ,if the pixel is bigger than the threshold set it 1,otherwise set it 0

bgr_img=cv2.imread("imori.jpg")
gray_img=cv2.cvtColor(bgr_img,cv2.COLOR_BGR2GRAY)
threshold=128
gray_img[gray_img<threshold]=0
gray_img[gray_img>threshold]=1

cv2.imshow("gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()