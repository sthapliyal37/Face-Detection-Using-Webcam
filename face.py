import cv2 

 #SIDDHANT THAPLIYAL
face_cascade = cv2.CascadeClassifier('pythonPro\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('pythonPro\haarcascade_eye.xml')
#banana_cascade = cv2.CascadeClassifier('pythonPro\haarcascade_banana_classifier.xml')
cap = cv2.VideoCapture(0) 
while 1: 
    
	ret, img = cap.read() 
        
	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA) 
	faces = face_cascade.detectMultiScale(gray,1.3,5)
	eye = eye_cascade.detectMultiScale(gray,1.3,5)
	#banana = banana_cascade.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
	        
            cv2.rectangle(img, (x, y), (x+w, y+h), (250, 0, 250), 0)
                
            font = cv2.FONT_HERSHEY_DUPLEX  # color
            cv2.putText(img, "PERSON", (x+w,y+h), font, 0.8, (0, 250, 0), 1)
        
        
            for (x,y,w,h) in eye:
	        
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 250), 0)
                
                font = cv2.FONT_HERSHEY_DUPLEX  # color
                cv2.putText(img, "Eye", (x+w,y+h), font, 0.8, (250, 250, 0), 1)
                
            
	cv2.imshow('OBJECT DETECTION',img) 

	k = cv2.waitKey(30) & 0xff
	if k == 27: 
		break


cap.release()  
cv2.destroyAllWindows() 
#SIDDHANT THAPLIYAL
#B.TECH(CSE)