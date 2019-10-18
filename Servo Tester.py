from Arduino import Arduino
from time import sleep

ServoS = [3,5,6,9,10,11]
delay = 0.01
arduino = Arduino()

for servo in ServoS:
    arduino.Servos.attach(servo)
    arduino.Servos.write(servo,0)

while True:

    for angle in range (0,180):
        print(angle)
        for servo in ServoS:
            arduino.Servos.write(servo,angle)
        sleep(delay)
    
    for angle in range (180,0,-1):
        print(angle)
        for servo in ServoS:
            arduino.Servos.write(servo,angle)
        sleep(delay)