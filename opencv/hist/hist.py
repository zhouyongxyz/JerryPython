#encoding:utf-8

#
#灰度图像直方图
#

from matplotlib import pyplot as plt
import cv2

image = cv2.imread("../images/jay.jpg")
cv2.imshow("Original",image)

#图像直方图
hist = cv2.calcHist([image],[0],None,[256],[0,256])

plt.figure()#新建一个图像
plt.title("Grayscale Histogram")#图像的标题
plt.xlabel("Bins")#X轴标签
plt.ylabel("# of Pixels")#Y轴标签
plt.plot(hist)#画图
plt.xlim([0,256])#设置x坐标轴范围
plt.show()#显示图像