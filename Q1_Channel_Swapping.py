import numpy as np
import cv2
#opencv processing img with [b,g,r],which is different with PIL ([r,g,b])
# so be care when you mix them to process image

#method1: split the image dims to change the channel
bgr_img = cv2.imread("imori.jpg")#img channel dim is(bgr)
rgb_img=bgr_img.copy()
b = bgr_img[:, :, 0].copy()
g = bgr_img[:, :, 1].copy()
r = bgr_img[:, :, 2].copy()
rgb_img[:, :, 0] = r
rgb_img[:, :, 1] = g
rgb_img[:, :, 2] = b

#method 2:using opencv cv2.cvtColor(srcBGR, cv2.COLOR_BGR2RGB)
rgb_img = cv2.cvtColor(bgr_img,cv2.COLOR_BGR2RGB)


# show two images in one window to make a comparision
imgs = np.concatenate((bgr_img,rgb_img), axis=1)
cv2.imshow("result", imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()
