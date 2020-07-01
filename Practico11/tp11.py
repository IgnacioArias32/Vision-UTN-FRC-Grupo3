import numpy as np
import cv2
#import opencv2_contrib

MIN_MATCH_COUNT = 10

img1 = cv2.imread('Calc.jpeg')
img1 = cv2.resize(img1, (820,460))
print(img1.shape)
img2 = cv2.imread('Calc2.jpeg')
img2 = cv2.resize(img2, (820,460))

gray1 = cv2.cvtColor ( img1,cv2.COLOR_BGR2GRAY) #Hacemos las imagenes grises, para encontrar puntos de interes
gray2 = cv2.cvtColor ( img2,cv2.COLOR_BGR2GRAY)

#dscr = # Inicializamos el detector y el descriptor

sift = cv2.xfeatures2d.SIFT_create()

#sift = cv2.ORB_create(nfeatures=1500)

kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher(cv2.NORM_L2)

matches = matcher.knnMatch(des1, des2, k=2)


good = []
for m, n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

vacia = np.zeros((img1.shape[0],img1.shape[1]*2),np.uint8)
img3= cv2.drawMatches(img1,kp1,img2,kp2,good[:50],vacia)
#cv2.imshow('Cubo2',img2)
#cv2.imshow('Cubo1',img1)
cv2.imshow('img3',img3)

if(len(good) > MIN_MATCH_COUNT):
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)

    wimg2 = cv2.warpPerspective(img2, H, (img1.shape[1],img1.shape[0])) # Aplicamos la transformación perspectiva H a la imagen 2

# Mezclamos ambas imágenes
    alpha = 0.5
    blend = np.array(wimg2 * alpha + img1 * (1 - alpha), dtype=np.uint8)

    cv2.imshow('Final',blend)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

else:
    print("NO HAY COINCIDENCIAS SUFICIENTES")



