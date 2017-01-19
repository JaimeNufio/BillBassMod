import RPi.GPIO as io;
import MotorControl as control;
import pygame
import time


io.setwarnings(False);

motor1 = [11,13];
motor2 = [29,31];
motor3 = [16,18];
motors = [motor1,motor2,motor3];

#pygame.init()
#pygame.display.set_mode((1,1))#screensize

control.initMotor(motors);

for motor in motors:
	control.motorForward(motor);

time.sleep(5);

for motor in motors:
	control.motorBackward(motor);


for motor in motors:
	control.motorOff(motor);

