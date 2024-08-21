import numpy as np

import cv2 as cv

img = cv.imread('people.jpg')
# 获取某个像素点
px = img[100, 100]
# 仅获取蓝色通道的强度值
blue = img[100, 100, 0]
print(blue)
# 修改某个位置的像素值
img[100, 100] = [255, 255, 255]
