import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#1读取图像
img1 = cv.imread('park.jpg')
#2创建核结构
kernel = np.ones((10,10),np.uint8)
#3图像的开闭运算
cvOpen = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel) #开运算
cvClose = cv.morphologyEx(img1, cv.MORPH_CLOSE, kernel) #闭运算

#图像展示
fig,axes = plt.subplots(nrows=2, ncols=2,figsize=(10,8))
axes[0, 0].imshow(img1)
axes[0, 0].set_title("原图")
axes[0, 1].imshow(cvOpen)
axes[0, 1].set_title("开运算结果")
axes[1, 0].imshow(img1)
axes[1, 0].set_title("原图")
axes[1, 1].imshow(cvClose)
axes[1, 1].set_title("闭运算结果")
plt.show()

