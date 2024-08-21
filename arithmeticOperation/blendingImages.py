import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# OpenCV 默认加载的图像格式是 BGR，而许多显示库和标准格式期望 RGB 图像
# 1读取图像
img1 = cv.imread('park.jpg')
img2 = cv.imread("rain.jpg")
if img1.shape != img2.shape:
    print("调整图片尺寸")
    img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))
if img1.shape[2] != img2.shape[2]:
    if img1.shape[2] == 3:  # img1是彩色的图像
        im2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)  # 将img转换成彩色
    else:  # img 是灰度图像
        img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)  # 将 img1 转换为灰度
        img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)  # 将 img2 转换为灰度
# 2图像混合
img3 = cv.addWeighted(img1, 0.7, img2, 0.3, 0)

# 图像显示
plt.figure(figsize=(8, 8))
# 将 BGR 图像转换为 RGB 图像
plt.imshow(img3[:, :, ::-1])
plt.show()
