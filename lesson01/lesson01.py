import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1、读取图像
img = cv.imread('people.jpg', cv.IMREAD_GRAYSCALE)  # 使用cv.IMREAD_GRAYSCALE明确读取灰度图像

# 2 显示图像
# 2.1 利用 OpenCV 显示图像
cv.imshow('image', img)
cv.waitKey(0)  # 等待按键，然后关闭窗口
cv.destroyAllWindows()  # 清除所有打开的窗口

# 2.2 在 matplotlib 中显示图像
# 由于 img 是灰度图像，不需要进行颜色通道的反转
plt.imshow(img, cmap='gray')  # 使用灰度颜色映射
plt.title('匹配结果')
plt.xticks([]), plt.yticks([])  # 移除坐标轴
plt.show()

# 3 保存图像
cv.imwrite('lena.jpg', img)