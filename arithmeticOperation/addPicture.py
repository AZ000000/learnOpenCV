import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# # np的add 和cv的add 的区别
# x = np.uint8([250])
# y = np.uint8([10])
# print(cv.add(x, y))
# print(x + y)

#两个图片相加

#1读取图像
img1 = cv.imread('park.jpg')
img2 = cv.imread('rain.jpg')

# 确保图像尺寸相同
if img1.shape != img2.shape:
    # 调整尺寸
    img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))  # 调整 img2 的尺寸以匹配 img1

# 确保图像通道数相同
if img1.shape[2] != img2.shape[2]:
    if img1.shape[2] == 3:  # img1 是彩色图像
        img2 = cv.cvtColor(img2, cv.COLOR_GRAY2BGR)  # 将 img2 转换为彩色
    else:  # img1 是灰度图像
        img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)  # 将 img1 转换为灰度
        img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)  # 将 img2 转换为灰度

#加法操作
img3 = cv.add(img1,img2) #cv中的加法
img4 = img1+img2 #两个图片直接相加

#3图像显示
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img3[:,:,::-1])
axes[0].set_title('cv中的加法')
axes[1].imshow(img4[:,:,::-1])
axes[1].set_title('直接相加')
plt.show()
