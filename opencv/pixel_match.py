import cv2

def pixel_match(templ,src):
    print("templ name = " + templ)
    img_templ = cv2.imread(templ,cv2.IMREAD_GRAYSCALE)
    img_src = cv2.imread(src,cv2.IMREAD_GRAYSCALE)
    img_templ_width = img_templ.shape[1]
    img_templ_height = img_templ.shape[0]

    center_x = int(img_templ_width/2)
    center_y = int(img_templ_height/2)
    print(img_templ_width,img_templ_height,center_x,center_y)
    center_rgb = img_templ[center_y,center_x]

    cv2.circle(img_templ,(center_x,center_y),5,(255,0,0))
    print(center_rgb)

    for i in range(0,img_src.shape[0]):
        for j in range(0,img_src.shape[1]):
            if img_src[i,j] == center_rgb:
                #print("center match = " , i , j)
                match = True
                for m in range(-10,10):
                    #for n in range(-30,30):
                    if i + m < img_src.shape[0] and img_src[i + m,j] != img_templ[center_y + m,center_x] :
                        #print("center match = " , i , j)
                        match = False
                # for m in range(-10, 10):
                #     # for n in range(-30,30):
                #     if j + m < img_src.shape[1] and img_src[i , j + m] != img_templ[center_y , center_x + m]:
                #         # print("center match = " , i , j)
                #         match = False
                if match :
                    print("center match = ", i, j)
                    cv2.rectangle(img_src,(j -center_y,i - center_x),(j + center_y,i + center_x),(0,0,0))
                    #cv2.rectangle(img_src, (i, j - 10), (i + 10, j + 10), (0, 0, 0))




    #cv2.imshow("templ",img_templ)
    cv2.imshow("src",img_src)
    cv2.imwrite("images/out.png",img_src)

    cv2.waitKey(0)
    pass


def main():
    pixel_match("images/templ_1.png","images/src.png")
    pass


if __name__ == "__main__":
    main()