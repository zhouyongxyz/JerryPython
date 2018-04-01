import cv2

def main():
    img = cv2.imread("images/baidustore/dianwo.png")
    cv2.imshow("test",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()