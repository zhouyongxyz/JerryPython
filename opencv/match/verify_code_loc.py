import cv2


def main():
    img = cv2.imread("../images/baidustore/verify_code_scene.png")

    cv2.imshow("verify code",img)
    cv2.waitKey(0)
    pass



if __name__ == '__main__':
    main()