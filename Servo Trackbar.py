from Arduino import Arduino
import time
import cv2 as cv

Servo1 = 5
Servo2 = 6

def nothing(x):
    pass    

cv.namedWindow('window',cv.WINDOW_FREERATIO)

cv.createTrackbar('Port10','window',0,255,nothing)
cv.createTrackbar('Port11','window',0,255,nothing)
cv.createTrackbar('Port12','window',0,128,nothing)
cv.createTrackbar('Port13','window',0,128,nothing)
cv.createTrackbar('Servo1v','window',0,180,nothing)
cv.createTrackbar('Servo2v','window',0,180,nothing)

arduino = Arduino()
arduino.Servos.attach(Servo1)
arduino.Servos.attach(Servo2)

while True:	    
    Port10 = cv.getTrackbarPos('Port10','window')  
    Port11 = cv.getTrackbarPos('Port11','window')
    Port12 = cv.getTrackbarPos('Port12','window')
    Port13 = cv.getTrackbarPos('Port13','window')
    Servo1v = cv.getTrackbarPos('Servo1v','window')
    Servo2v = cv.getTrackbarPos('Servo2v','window')

    arduino.analogWrite(10,Port10)
    arduino.analogWrite(11,Port11)
    arduino.analogWrite(12,Port12)
    arduino.analogWrite(13,Port13)
    
    arduino.Servos.write(Servo1, Servo1v)
    arduino.Servos.write(Servo2, Servo2v)

    #print(arduino.Servos.read(Servo1))

    if cv.waitKey(128) == ord("q"):
        arduino.Servos.detach(Servo1)
        arduino.Servos.detach(Servo2)
        cv.destroyAllWindows()
        break