import numpy as np
import cv2

ix, iy = -1, -1
i=1
j=1
c1 = [239, 614]
c2 = [541, 460]
c3 = [36, 157]
c4 = [316, 148]

c1m = [-1, -1]
c2m = [-1, -1]

medir=False
midiendo=False
distanciax=0.0
distanciay=0.0
transformada=0

def click(event, x, y, flags, param):
    global medir,c1m,c2m,j,distanciax,distanciay,transformada

    if medir is True:
        if event == cv2.EVENT_LBUTTONDOWN:
            if j==1:
                c1m=(x,y)
                cv2.rectangle(Transformada, (x, y), (x+2, y+2), (0, 0, 255),-1)
                cv2.imshow('Paramedir', Transformada)
                j=j+1
            elif j==2:
                c2m=(x,y)
                cv2.rectangle(Transformada, (x, y), (x+2, y+2), (0, 0, 255),-1)
                cv2.imshow('Paramedir', Transformada)
                j=j+1

    return


def TransformacionProyectiva(image):
    (h,w) = image.shape[:2]
    pts1 = np.float32([[c1], [c2], [c3], [c4]])
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(image, M, (w,h))
    dst = cv2.flip(dst,0)
    return dst


def Medir():
    patronpx=244.0
    patroncm=9.1
    distanciax=c2m[0]-c1m[0]
    distanciay=c2m[1]-c1m[1]
    distanciaxcm=distanciax*patroncm/patronpx
    distanciaycm=distanciay*patroncm/patronpx
    distanciatotalcm=math.sqrt((distanciaxcm*distanciaxcm)+(distanciaycm*distanciaycm))
    print('Medida Horizontal:',abs(distanciaxcm))
    print('Medida Vertical:',abs(distanciaycm))
    print('Distancia entre los puntos:',abs(distanciatotalcm))


    # main



cv2.namedWindow ('Paramedir')
Paramedir =cv2.imread('Paramedir.jpeg', 1)
(h, w) = Paramedir.shape[:2]
cv2.imshow('Paramedir', Paramedir)
cv2.setMouseCallback('Paramedir',click)
print('Presione m para empezar a medir')




while (1):
    k = cv2.waitKey(1) & 0xFF
    if midiendo==False:
        cv2.imshow('Paramedir', Paramedir)
    if k == ord('m'):
        Transformada = TransformacionProyectiva(Paramedir)
        cv2.imshow('Paramedir',Transformada)
        medir=True
        midiendo=True
    if j==3:
        Medicion=Medir(Transformada)
        cv2.imwrite('SalidaTp9.png',Transformada)
        j=1

    if k == ord('r'):
        Paramedir = cv2.imread('Paramedir.jpeg', 1)
        cv2.imshow('Paramedir', Paramedir)
        midiendo=False
        medir=False
    if k == ord('q'):
        break

