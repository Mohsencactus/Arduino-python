from Arduino import Arduino
import time
import cv2 as cv

def nothing(x):
    pass    

cv.namedWindow('window',cv.WINDOW_FREERATIO)

cv.createTrackbar('Port2','window',0,128,nothing)
cv.createTrackbar('Port3','window',0,255,nothing)
cv.createTrackbar('Port4','window',0,128,nothing)
cv.createTrackbar('Port5','window',0,255,nothing)
cv.createTrackbar('Port6','window',0,255,nothing)
cv.createTrackbar('Port7','window',0,128,nothing)
cv.createTrackbar('Port8','window',0,128,nothing)
cv.createTrackbar('Port9','window',0,128,nothing)
cv.createTrackbar('Port10','window',0,255,nothing)
cv.createTrackbar('Port11','window',0,255,nothing)
cv.createTrackbar('Port12','window',0,128,nothing)
cv.createTrackbar('Port13','window',0,128,nothing)

arduino = Arduino()

while True:	    
    Port2 = cv.getTrackbarPos('Port2','window')  
    Port3 = cv.getTrackbarPos('Port3','window')
    Port4 = cv.getTrackbarPos('Port4','window')  
    Port5 = cv.getTrackbarPos('Port5','window')
    Port6 = cv.getTrackbarPos('Port6','window')  
    Port7 = cv.getTrackbarPos('Port7','window')
    Port8 = cv.getTrackbarPos('Port8','window')
    Port9 = cv.getTrackbarPos('Port9','window')
    Port10 = cv.getTrackbarPos('Port10','window')  
    Port11 = cv.getTrackbarPos('Port11','window')
    Port12 = cv.getTrackbarPos('Port12','window')
    Port13 = cv.getTrackbarPos('Port13','window')

    arduino.analogWrite(2,Port2)
    arduino.analogWrite(3,Port3)
    arduino.analogWrite(4,Port4)
    arduino.analogWrite(5,Port5)
    arduino.analogWrite(6,Port6)
    arduino.analogWrite(7,Port7)
    arduino.analogWrite(8,Port8)
    arduino.analogWrite(9,Port9)
    arduino.analogWrite(10,Port10)
    arduino.analogWrite(11,Port11)
    arduino.analogWrite(12,Port12)
    arduino.analogWrite(13,Port13)

    if cv.waitKey(128) == ord("q"):
        cv.destroyAllWindows()
        break