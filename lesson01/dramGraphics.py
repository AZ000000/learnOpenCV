import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1创建一个空白的图像
img = np.zeros((512, 512, 3), np.uint8)

# 2绘制图形
# 2.1绘制线条
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# 2.2绘制三角形
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# 2.3绘制园
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

# 3图像展示
plt.imshow(img[:, :, ::-1])
plt.title('匹配结果'), plt.xticks([]), plt.yticks([])
plt.show()
