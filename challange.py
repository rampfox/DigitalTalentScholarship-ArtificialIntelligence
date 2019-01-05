import cv2
import numpy as np
from matplotlib import pyplot as plt

video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    # Display the resulting frame
    cv2.imshow('Video', frame)
    
img = cv2.imread('/Users/Alwi/Desktop/DIP/Topik/zzz.jpg',0)
template = cv2.imread('/Users/Alwi/Desktop/DIP/Topik/zzz1.jpg',0)
w, h = template.shape[::-1]
#Apply template Matching
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.4999
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    img=cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (200,150,255),2)
#Showing
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
	
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break