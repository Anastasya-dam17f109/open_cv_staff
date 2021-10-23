import cv2
import numpy as np


img = cv2.imread("D:/classification_image_item1.jpg")
'''
# отражение картинки - 0 горизонталь, 1 вертикаль, -1 - все
#img = cv2.flip(img,0 )
# поворот - афинное преобразование
def rotate(img, angle):
    height, width = img.shape[:2]
    point = (width//2, height//2)
    mat = cv2.getRotationMatrix2D(point,angle,1)
    return cv2.warpAffine(img, mat, (width , height))
# смещение - аффинное преобразование
def transform(img, x, y):
    height, width = img.shape[:2]
    mat = np.float32([[1,0,x],[0,1,y]])
    return cv2.warpAffine(img, mat, (width , height))

#img = rotate(img, 45)
img = transform(img, 45, -90)
'''


# контуры
'''
для поиска контуров необходимо упрощать картинку
1. приводить ее к одному каналу
2. чуть-чуть ее размывать - чтобы удалить шум и сгладить лишние выбросы, которые
приведут к появлению маленьких лишних контуров
'''
'''
построение контуров по углам
con, - список контуров
hir - иерархия объектов
'''
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
new_img = np.zeros(img.shape, dtype= 'uint8')
img = cv2.GaussianBlur(img, (5, 5),0)
img = cv2.Canny(img, 100,140)

gg, con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img,con,-1,(255,130,29),1)
cv2.imshow("classification result", new_img)
# бесконечное отображение
cv2.waitKey(0)