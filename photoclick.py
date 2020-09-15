import cv2
x=cv2.VideoCapture(0)
ret,photo=x.read()
cv2.imwrite('/root/Desktop/myphoto.png',photo)
x.release()
