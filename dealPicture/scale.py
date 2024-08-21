import cv2 as cv
import matplotlib.pyplot as plt
# 1读取图片
img1 = cv.imread('people.jpg')

# 2图片缩放
# 2.1绝对尺寸
rows, cols = img1.shape[:2]
res = cv.resize(img1, (2 * cols, 2 * rows), interpolation=cv.INTER_CUBIC)

# 2.2相似尺寸
res1 = cv.resize(img1, None, fx=0.5, fy=0.5)

# 3 图像显示
# 3.1使用opencv显示图像(不推荐)
# cv.imshow('original', img1)
# cv.imshow('enlarge', res)
# cv.imshow('shrink', res1)
# cv.waitKey(0)

# 3.2使用matplotlib显示图像
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 8), dpi=100)
axes[0].imshow(res[:, :, ::-1])
axes[0].set_title("绝对尺度（放大）")
axes[1].imshow(img1[:, :, ::-1])
axes[1].set_title("原图")
axes[2].imshow(res1[:, :, ::-1])
axes[2].set_title("相对尺度（缩小）")
plt.show()
