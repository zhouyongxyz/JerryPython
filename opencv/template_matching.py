#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import cv2
import numpy as np

def match(source,templ):
    source = cv2.imread(source, cv2.IMREAD_COLOR);
    template = cv2.imread(templ, cv2.IMREAD_COLOR);

    #result = cv2.Mat();

    result_cols = source.cols - template.cols + 1;
    result_rows = source.rows - template.rows + 1;
    result = cv2.create(result_cols, result_rows, cv2.CV_32FC1);

    cv2.matchTemplate(source, template, result, cv2.TM_SQDIFF_NORMED); # 这里我们使用的匹配算法是标准平方差匹配
    # method = CV_TM_SQDIFF_NORMED，数值越小匹配度越好
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1,cv2.Mat());


    minMaxLocResult = cv2.minMaxLoc(result, cv2.Mat());


    print("匹配度：" + minMaxLocResult.minVal);
    matchLoc = minMaxLocResult.minLoc;

    x = -1;
    y = -1;
    if (minMaxLocResult.minVal >= 0 and minMaxLocResult.minVal < 4.0E-8) :
        cv2.rectangle(source, matchLoc, cv2.Point(matchLoc.x + template.cols(), matchLoc.y + template.rows()), cv2.Scalar(0, 255, 0), 2, 8, 0);
        x = matchLoc.x + template.cols() / 2;
        y = matchLoc.y + template.rows() / 2;
    else :
        print("targetImageMatch not match .");
    cv2.imshow("result",source)
    pass


def main() :
    source = "images/baidustore/search_scene.png"
    templ = "images/baidustore/search.png"

    match(source,templ)

    pass

if __name__ == "__main__":
    main()
