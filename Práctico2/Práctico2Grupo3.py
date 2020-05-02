import sys
import cv2

img=cv2.imread('rana.jpg', 0)
cv2.imshow('image', img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
for row in range(1, len(img)):
    for line in range(1, len(img[0])):
        if img[row,line]<225:   #No utilizamos 255 debido a que el fondo tiene pixeles que no son totalmente blancos
            img[row,line]=0
        else:
            img[row,line]=255
cv2.imwrite('resultado.jpg', img )
cv2.imshow('image', img)
cv2.waitKey(3000)
