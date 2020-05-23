import cv2


ix , iy = -1, -1
def recortar ( event , x , y , flags , param ) :
    global ix , iy , crop_img
    if event == cv2.EVENT_LBUTTONDOWN:
        ix , iy = x , y

    elif event == cv2.EVENT_LBUTTONUP:
                crop_img = img[iy:y, ix:x]
                cv2.rectangle(img, (ix-1, iy-1), (x+1, y+1), (0, 0, 255),1) #Se suma 1 a las esquinas para que no se vea el rectangulo en el recorte
                cv2.imshow('image', img)

img=cv2.imread('rana.jpg', 1)

cv2.namedWindow ('image')
cv2.setMouseCallback ('image', recortar )
cv2.imshow('image', img )
while ( 1 ) :
    cv2.setMouseCallback('image', recortar)
    k = cv2.waitKey ( 1 ) &0xFF
    if k == ord ( 'g' ):
        cv2.imwrite('Recorte.jpg', crop_img)
        cv2.destroyAllWindows()
        cv2.namedWindow('image')
        cv2.imshow('image', crop_img)
        k = cv2.waitKey(0)
    if k == ord('r'):
        cv2.imshow('image', img)
    elif k== ord('q'):
        break

cv2.destroyAllWindows ( )

