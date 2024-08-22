import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 1. 直接以灰度图的方式读入
img = cv.imread('park.jpg', 0)

# 2. 均衡化处理
dst = cv.equalizeHist(img)

# 3. 结果展示
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8), dpi=100)

# 显示原始图像
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title("原图")

# 显示均衡化后的图像
axes[0, 1].imshow(dst, cmap='gray')
axes[0, 1].set_title("均衡化后结果")

# 移除坐标轴
for ax in axes.flat:
    ax.axis('off')

# 显示图表
plt.show()