import cv2
import numpy as np
#img = cv2.imread("D:/classification_image_item1.jpg")
#cv2.imshow("classification result", img)
# бесконечное отображение
#cv2.waitKey(0)
# отображенеи на 5 сек
#cv2.waitKey(5000)

'''
# звятие видео с вебки
cap = cv2.VideoCapture(0)
# установка ширины окна
cap.set(2,500)
cap.set(3, 300)

# цикл показа видео
while  True:
    # считывание кадра
    sucsess,img = cap.read( )
    cv2.imshow("me", img)
    # установка времени проигрывания и клавиши на выход
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
'''
# изменение размеров картинки
img = cv2.imread("D:/classification_image_item1.jpg")
new_img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
cv2.imshow("classification result", img)
cv2.imshow("little result", new_img)
cv2.waitKey(0)
'''
'''
# добавление эффекта размытия на изображение
img = cv2.imread("D:/classification_image_item1.jpg")
# размытие с фильтрацией гауссовским фильтром - (9, 9) -аппертура фильтра, 0 - пасаметрр сигма, в данном случаке opencv сам его считает
#img = cv2.GaussianBlur(img, (9, 9),0)
# превращение картинки в серую - здесь происходит определенным образом смешение цветовых каналов, ни один целиком не берется
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# детектор углов - детектор, разработанный John F. Canny
img = cv2.Canny(img, 90,90)
# дополнительное  увеличение обводки контуров - жирность
# нужно для соединения отдельных частей объекта - например разрозненных контуров
kernel = np.ones((5,5) , np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
# уменьшение  обводки контуров - жирность- убираем лишние линии,
# которые покрываем первой функцией
img = cv2.erode(img, kernel, iterations=1)
cv2.imshow("classification result", img)
cv2.waitKey(0)
'''


# звятие видео с вебки
cap = cv2.VideoCapture(0)
# установка ширины окна
cap.set(2,500)
cap.set(3, 300)

# цикл показа видео
while  True:
    # считывание кадра
    sucsess,img = cap.read( )
    img = cv2.GaussianBlur(img, (9, 9),0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("me", img)
    # установка времени проигрывания и клавиши на выход
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
