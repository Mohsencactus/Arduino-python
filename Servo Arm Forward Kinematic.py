from Arduino import Arduino
from time import sleep

servo = [3,5,6,9]
links = [5,6,9]
home = [55,107,97,93]
delay = 0.01

arduino = Arduino()

for i in range (len(servo)):
    arduino.Servos.attach(servo[i])
    arduino.Servos.write(servo[i],home[i])

while True:
    i = int(input("Servo: "))
    angle = int(input("Angle: "))
    arduino.Servos.write(links[i-1],angle)
    print(angle)
    sleep(delay)