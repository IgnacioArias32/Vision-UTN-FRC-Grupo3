import sys
import cv2

filename = 'video.mp4'
cap = cv2.VideoCapture(filename)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height =int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = int(cap.get(cv2.CAP_PROP_FPS))

print(width,height, fps)

framesize = (width, height)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, framesize)
delay = fps
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)
        cv2.imshow('Image gray', gray)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
