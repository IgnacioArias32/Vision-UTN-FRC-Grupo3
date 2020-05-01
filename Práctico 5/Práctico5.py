import numpy as np
import cv2


def translate(image, x, y):
    (h, w) = (image.shape[0], image.shape[1])
    M = np.float32([[1, 0, x],
                    [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (w, h))
    return shifted


def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def Euclidian(image, angle, x, y):

    traslacion = translate(image, x, y)
    Euclidia = rotate(traslacion, angle)
    return Euclidia

    # main


img = cv2.imread('rana.jpg', 1)
ang = int(input('Ingrese el angulo de rotación: '))
x = int(input('Ingrese el valor de x de la traslacion: '))
y = int(input('Ingrese el valor de y de la traslacion: '))

Euclidana=Euclidian(img,ang,x,y)
cv2.imshow('Euclidia', Euclidana)
cv2.waitKey(0)
