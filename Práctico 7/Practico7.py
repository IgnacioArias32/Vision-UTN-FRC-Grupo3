import numpy as np
import cv2

ix, iy = -1, -1
i=1
c1 = [-1, -1]
c2 = [-1, -1]
c3 = [-1, -1]
mode=False

def click(event, x, y, flags, param):
    global c1,c2,c3,i,mode

    if mode is True:
        if event == cv2.EVENT_LBUTTONDOWN:
            if i==1:
                c1=(x,y)
                cv2.rectangle(cartel, (x, y), (x+2, y+2), (0, 255, 0),-1)
                i=i+1
            elif i==2:
                c2=(x,y)
                cv2.rectangle(cartel, (x, y), (x+2, y+2), (0, 255, 0),-1)
                i=i+1
            elif i==3:
                c3=(x,y)
                cv2.rectangle(cartel, (x, y), (x+2, y+2), (0, 255, 0),-1)
                i=i+1
    return


def TransformacionAfin(image):
    (h, w) = image.shape[:2]
    image = cv2.flip(image,0)
    pts1 = np.float32([[0,0], [w,h], [0,h]])
    pts2 = np.float32([[c1], [c2], [c3]])
    M = cv2.getAffineTransform(pts1, pts2)
    afinada = cv2.warpAffine(image, M, (w,h))
    return afinada
    # main



cv2.namedWindow ('cartel')
cartel =cv2.imread('CARTEL.jpg', 1)
cv2.imshow('cartel', cartel)
cv2.setMouseCallback('cartel',click)
(h, w) = cartel.shape[:2]
img = cv2.imread('publicidad.jpg', 1)
img = cv2.resize(img, (w, h))


while (1):
    cv2.imshow('cartel', cartel)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('a'):
        mode=True
    if i==4:
        Transformada = TransformacionAfin(img)
        cv2.imwrite('mask.png',Transformada)
        mask=cv2.imread('mask.png',0)
        for row in range(1, len(mask)):
            for line in range(1, len(mask[0])):
                if mask[row,line]<1:
                    mask[row, line] = 255
                else:
                    mask[row, line] = 0
        cv2.imwrite('mask.png', mask)
        mask=cv2.imread('mask.png',1)
        mask=cv2.bitwise_and(mask,cartel)
        Transformada=cv2.addWeighted(mask,1, Transformada,1, 0)
        cv2.imshow('cartel', Transformada)
        cv2.waitKey(0)
        cv2.imwrite('SalidaTp7.jpg', Transformada)
        i=1
        mode=False
    if k == ord('q'):
        break




