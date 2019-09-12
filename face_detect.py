import cv2

cv2.namedWindow('FaceDetect')
img = cv2.imread('lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
faces = face_cascade.detectMultiScale(gray)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
cv2.imshow('FaceDetect',img)

while chr(cv2.waitKey(0)) != 'q':
	continue
	
cv2.destroyAllWindows()
