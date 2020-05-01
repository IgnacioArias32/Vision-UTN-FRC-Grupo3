import numpy as np
import cv2

ix , iy = -1, -1

def recortar ( event , x , y , flags , param ) :
    global ix , iy , crop_img
    if event == cv2.EVENT_LBUTTONDOWN:
        ix , iy = x , y
    elif event == cv2.EVENT_MOUSEMOVE:
                crop_img = img[iy:y, ix:x]


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


img=cv2.imread('rana.jpg', 1)

angle = int(input('Ingrese el angulo de rotación: '))
xin = int(input('Ingrese el valor de x de la traslacion: '))
yin = int(input('Ingrese el valor de y de la traslacion: '))

cv2.namedWindow ('image')
cv2.setMouseCallback ('image', recortar )
cv2.imshow('image', img )
while ( 1 ) :
    cv2.setMouseCallback('image', recortar)
    k = cv2.waitKey ( 1 ) &0xFF
    if k == ord ( 'g' ):
       # cv2.imwrite('Recorte.jpg', crop_img)
       # cv2.destroyAllWindows()
     #   cv2.namedWindow('image')
     #   cv2.imshow('image', crop_img)
        k = cv2.waitKey(0)
    if k == ord('e'):
        Transformada=Euclidian(crop_img,angle,xin,yin)
        cv2.imshow('image', Transformada)
        cv2.imwrite('SalidaTp5.jpg',Transformada)
    elif k== ord('q'):
        break
cv2.destroyAllWindows ( )
