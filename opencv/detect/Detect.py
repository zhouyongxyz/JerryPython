import cv2
import time
import datetime
import os
import easygui


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        ("---  new folder...  ---")
        print
        ("---  OK  ---")

    else:
        print
        ("---  There is this folder!  ---")


file = "D:\\CCTVlook"  # 保存位置
mkdir(file)
print("文件储存于D:\\CCTVlook")
# 选取摄像头，0为笔记本内置的摄像头，1,2···为外接的摄像头
camera = cv2.VideoCapture(0)
title = easygui.msgbox(msg="将于5s后开始记录摄像头移动情况！""\n""请离开保证背景稳定""\n"
                       , title="运动检测追踪拍照", ok_button="开始执行")
msg = easygui.msgbox(msg="移动物体保存于D:\\CCTVlook")
time.sleep(5)  # 延迟5s执行
background = None  # 初始化背景


def nothing(x):
    pass


cv2.namedWindow("fps")  # 新建一个窗口
cv2.createTrackbar('level', 'fps', 21, 255, nothing)  # 新建阈值滑动条
shot_idx = 0
prev_frame = None
center = None
prev_point = (0,0)

while True:
    text = "No Target"
    flat = 0
    # 滑动条赋值
    kerne = cv2.getTrackbarPos('level', 'fps')
    if kerne % 2 == 0:
        kerne = kerne + 1  # 解决滑动条赋值到高斯滤波器是偶数异常抛出
    (grabbed, frame) = camera.read()
    # 对帧进行预处理，先转灰度图，再进行高斯滤波。
    # 用高斯滤波对图像处理，避免亮度、震动等参数微小变化影响效果
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (kerne, kerne), 0)
    # 将第一帧设置为整个输入的背景
    if background is None:
        background = gray
        prev_frame = gray
        continue

    # 当前帧和第一帧的不同它可以把两幅图的差的绝对值输出到另一幅图上面来
    frameDelta = cv2.absdiff(background, gray)
    # 二值化
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    # 腐蚀膨胀
    thresh = cv2.dilate(thresh, None, iterations=2)
    # 取轮廓
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]

    # 当前帧和第一帧的不同它可以把两幅图的差的绝对值输出到另一幅图上面来
    frameDelta2 = cv2.absdiff(prev_frame, gray)
    #cv2.imshow("frameDelta2", frameDelta2)
    # 二值化
    thresh2 = cv2.threshold(frameDelta2, 25, 255, cv2.THRESH_BINARY)[1]
    # 腐蚀膨胀
    thresh2 = cv2.dilate(thresh2, None, iterations=2)
    # 取轮廓
    cnts2 = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]


    cv2.imshow("thrresh2",thresh2)
    prev_frame = gray

    for b in cnts2:
        if cv2.contourArea(b) < 1800:  # 对于较小矩形区域，选择忽略
           continue
        flat = 1  # 设置一个标签，当有运动的时候为1
        # 计算轮廓的边界框，在当前帧中画出该框
        (x, y, w, h) = cv2.boundingRect(b)
        xx = (int) (x + w/2)
        yy = (int) (y + h/2)
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.line(frame,prev_point,(xx,yy),(0, 0, 255))
        prev_point = (xx,yy)
        #text = "Find Target! save as D:\CCTVlook"
        #print("Find Target!")

    cv2.imshow("thrresh233", frame)

    # 遍历轮廓
    for c in cnts:
        if cv2.contourArea(c) < 2800:  # 对于较小矩形区域，选择忽略
            continue
        flat = 1  # 设置一个标签，当有运动的时候为1
        # 计算轮廓的边界框，在当前帧中画出该框
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        text = "Find Target! save as D:\CCTVlook"
        #print("Find Target!")
    cv2.putText(frame, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    # cv2.imshow("Frame Delta", frameDelta)

    cv2.imshow("fps", frame)
    # cv2.imshow("Thresh", thresh)

    key = cv2.waitKey(1) & 0xFF

    # 如果q键被按下，跳出循环
    ch = cv2.waitKey(1)
    if key == ord("q"):
        break

    if flat == 1:  # 设置一个标签，当有运动的时候为1
        #fn = 'D:\CCTVlook\shot%d.jpg' % (shot_idx)
        #cv2.imwrite(fn, frame)
        shot_idx += 1
        continue
camera.release()
cv2.destroyAllWindows()
