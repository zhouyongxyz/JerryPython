#encoding:utf-8

#
#图像直方图均衡化
#

import numpy as np
import cv2

image = cv2.imread("../images/jay.jpg",0)#读取灰度图像
cv2.imshow("Original",image)
cv2.waitKey(0)

eq = cv2.equalizeHist(image)#灰度图像直方图均衡化
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)