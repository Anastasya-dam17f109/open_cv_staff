import cv2
import numpy as np

#photo = cv2.imread("D:/classification_image_item1.jpg")
'''
img0 = np.zeros((500,300), dtype = 'uint8')
circle = cv2.circle(img0.copy(), (0,0), 190, 255, cv2.FILLED)
square = cv2.rectangle(img0.copy(), (125,125),(225,225), 255,cv2.FILLED)
'''
 # вывод одинаковых участков изображений - эквивалентно наложению маски
#img = cv2.bitwise_and(circle, square)
# объединение участков изображений
#img = cv2.bitwise_or(circle, square)
# объединение с вычетом общей части участков изображений
#g = cv2.bitwise_xor(circle, square)
#объединение photo с самим собой по маске
#img = cv2.bitwise_and(photo,photo, mask =circle)
#cv2.imshow("result",img )
#cv2.waitKey(0)

# звятие видео с вебки
cap = cv2.VideoCapture(0)
# установка ширины окна
cap.set(2,500)
cap.set(3, 300)
sucsess,img = cap.read( )
img0 = np.zeros(img.shape[:2], dtype='uint8')
circle = cv2.circle(img0, (0, 0), 190, 255, cv2.FILLED)
# цикл показа видео
while  True:
    # считывание кадра
    sucsess,img = cap.read( )
    #img0 = np.zeros((int(cap.get(3)), int(cap.get(4))), dtype='uint8')
    #circle = cv2.circle(img0.copy(), (0, 0), 190, 255, cv2.FILLED)
    img1 = cv2.bitwise_and(img, img, mask=circle)
    cv2.imshow("me", img1)
    # установка времени проигрывания и клавиши на выход
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break