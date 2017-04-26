import RPi.GPIO as io;
import MotorControl as control;
import pygame
import time

pygame.init();
pygame.display.set_mode((1,1));

motor1 = [17,27];
motor2 = [5,6];
motor3 = [23,24];
motors = [motor1,motor2,motor3];

control.initMotor(motors);

for motor in motors:
	control.motorForward(motor);

time.sleep(1);

for motor in motors:
	control.motorBackward(motor);
time.sleep(1);

control.end(motors);

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
					control.motorForward(motor1)

