import cv2
import numpy as np


img = np.zeros((450,450,3), dtype = 'uint8')
'''
h = 256/450

for i in range(450):
    for j in range(450):
        img[i,j,2] = j*h
'''
'''
cv2. shape - вначале высота, потом ширина
cv2. resixe - -вначале ширина, потом высота
при записи из numpy ходим по принципу cv2. shape
'''
'''
# обводка координаты как cv2.shape
#cv2.rectangle(img, (0,0),(100,100), (0,255,0), thickness = 3)
# заливка
cv2.rectangle(img, (50,70),(100,100), (0,255,0), thickness = cv2.FILLED)
# линия - координаты как cv2. resixe
cv2.line(img, (200,0), (200,200),(255,0,0), thickness = 3)
# круг
cv2.circle(img, (400,300), 30,(0,255,0), thickness = cv2.FILLED)
# создание текста
cv2.putText(img, "Hello, Nastya!", (200,300), cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255), 1)
'''
cv2.rectangle(img, (img.shape[0]//2-90,img.shape[1]//2-90),(img.shape[0]//2+90,img.shape[1]//2+90), (0,255,0), thickness = 3)
cv2.circle(img, (img.shape[1]//2,img.shape[0]//2), 90,(8, 251, 255), thickness = 2)
cv2.line(img, (img.shape[0]//2-90,img.shape[1]//2-90),(img.shape[0]//2+90,img.shape[1]//2+90),(0,0,255), thickness = 3)
cv2.line(img, (img.shape[0]//2+90,img.shape[1]//2-90),(img.shape[0]//2-90,img.shape[1]//2+90),(0,0,255), thickness = 3)
cv2.putText(img, "Hello, Nastya!", (img.shape[1]//2-110,img.shape[0]//2), cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255), 1)
cv2.imshow("Image", img)
cv2.waitKey(0)