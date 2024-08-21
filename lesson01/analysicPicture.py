import cv2
import numpy as np

lena = cv2.imread('people.jpg', 0)
cv2.imshow('lena', lena)

r, c = lena.shape
list_img = []  # 生成一个空列表，保存用循环生成的每个位图
for i in range(8):
    mat = np.ones((r, c), dtype=np.uint8) * 2 ** i  # 生成提取矩阵mat
    bit_img = cv2.bitwise_and(lena, mat)  # 原始图像与提取矩阵进行按位与运算，得到对应位上的数据。！！！注意
    bit_img[bit_img[:, :] != 0] = 255
    list_img.append(bit_img)

cv2.imshow('lena0', list_img[0])
cv2.imshow('lena1', list_img[1])
cv2.imshow('lena2', list_img[2])
cv2.imshow('lena3', list_img[3])
cv2.imshow('lena4', list_img[4])
cv2.imshow('lena5', list_img[5])
cv2.imshow('lena6', list_img[6])
cv2.imshow('lena7', list_img[7])
cv2.waitKey(30000)
cv2.destroyAllWindows()
