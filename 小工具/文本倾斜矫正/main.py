# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:02:48 2020

@author: lei
"""


import numpy as np
import cv2
import math


def rotate(image, angle, center=None, scale=1.0):
    (w, h) = image.shape[0:2]
    if center is None:
        center = (w//2, h//2)
    wrapMat = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, wrapMat, (h, w))

# 使用霍夫变换
def getCorrect(read_path, save_path):
    # 读取图片，灰度化
    src = cv2.imread(read_path, cv2.IMREAD_COLOR)
    gray = cv2.imread(read_path, cv2.IMREAD_GRAYSCALE)
    # 腐蚀、膨胀
    kernel = np.ones((5, 5), np.uint8)
    erode_Img = cv2.erode(gray, kernel)
    eroDil = cv2.dilate(erode_Img, kernel)
    # 边缘检测
    canny = cv2.Canny(eroDil, 50, 150)
    # 霍夫变换得到线条
    lines = cv2.HoughLinesP(canny, 0.8, np.pi / 180, 90,
                            minLineLength=100, maxLineGap=10)
    drawing = np.zeros(src.shape[:], dtype=np.uint8)
    # 画出线条
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(drawing, (x1, y1), (x2, y2),
                 (0, 255, 0), 1, lineType=cv2.LINE_AA)

    """
    计算角度,因为x轴向右，y轴向下，所有计算的斜率是常规下斜率的相反数，我们就用这个斜率（旋转角度）进行旋转
    """
    k = float(y1-y2)/(x1-x2)
    thera = np.degrees(math.atan(k))

    """
    旋转角度大于0，则逆时针旋转，否则顺时针旋转
    """
    rotateImg = rotate(src, thera)
    cv2.imwrite(save_path, rotateImg)



if __name__ == "__main__":
    getCorrect('test.png', 'output.jpg')