import MotorControl as control
import pygame
import time

motor1 = [17,27];
motor2 = [5,6]
motor3 = [24,23]
motors = [motor1,motor2,motor3];
motorState = [False,False,False];

pygame.init()
pygame.display.set_mode((1,1))#screensize
running = True
active = True
 
control.initMotor(motors);

try:
    while True:
        control.motorOn(motor2)



except KeyboardInterrupt:
    pass

control.end(motors)
print("end")
