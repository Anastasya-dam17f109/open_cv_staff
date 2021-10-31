import cv2
import numpy as np

img = cv2.imread("D:/classification_image_item1.jpg")
# различные известные форматы хранения - HSV
#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#различные известные форматы хранения - LAB
#img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# разбиение 3хслойной картинка на слои
#
r,g,b = cv2.split(img)
# объединение слоев
img = cv2.merge([r,g,b])
cv2.imshow("classification result", img)

cv2.waitKey(0)