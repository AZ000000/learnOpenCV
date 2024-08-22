import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# 1 直接以灰度图的方式读入
img = cv.imread('park.jpg',0)
# 2 统计灰度图
histr = cv.calcHist([img],[0],None,[256],[0,256])
# 3 绘制灰度图
plt.figure(figsize=(10,6),dpi=100)
plt.plot(histr)
plt.grid()
plt.show()
