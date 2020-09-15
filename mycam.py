import cv2
x=cv2.VideoCapture(0)
while True:
	ret,photo=x.read()
	photo[0:100,0:100]=photo[150:250,250:350]
	cv2.imshow('hi',photo)
	if cv2.waitKey(1)==13:
		break

cv2.destroyAllWindows()
x.release()
