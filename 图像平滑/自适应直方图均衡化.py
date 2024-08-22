
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 1. 以灰度图形式读取图像
img = cv.imread('park.jpg',0)
# 2. 创建一个自适应均衡化的对象，并应用于图像
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
# 3. 图像展示
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img,cmap=plt.cm.gray)
axes[0].set_title("原图")
axes[1].imshow(cl1,cmap=plt.cm.gray)
axes[1].set_title("自适应均衡化后的结果")
plt.show()
