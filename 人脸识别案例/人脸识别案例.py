import cv2 as cv
import matplotlib.pyplot as plt

# 加载分类器
face_cas = cv.CascadeClassifier('D:/pythonProject/face/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
eyes_cas = cv.CascadeClassifier('D:/pythonProject/face/opencv/sources/data/haarcascades/haarcascade_eye.xml')

# 检查分类器是否加载成功
if face_cas.empty() or eyes_cas.empty():
    raise IOError('Unable to load the face/eye cascade classifiers.')

# 读取图片
img = cv.imread("people.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 调用识别人脸
faceRects = face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

# 绘制人脸框
for faceRect in faceRects:
    x, y, w, h = faceRect
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # 在识别出的人脸中进行眼睛的检测
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eyes_cas.detectMultiScale(roi_gray)

    # 绘制眼睛框
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# 显示结果
plt.figure(figsize=(8, 6), dpi=100)
plt.imshow(img[:, :, ::-1])
plt.title('检测结果')
plt.xticks([]), plt.yticks([])
plt.show()