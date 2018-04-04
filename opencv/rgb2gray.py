import cv2
img = cv2.imread("qn1.png", cv2.IMREAD_GRAYSCALE)
cv2.imwrite('qn1_gray.png', img)