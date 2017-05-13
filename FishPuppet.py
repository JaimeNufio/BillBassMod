import RPi.GPIO as io;
import MotorControl as control
import pygame
import time
import pyttsx

"""
engine = pyttsx.init()

def speak(words):
	engine.say(words)
	engine.runAndWait();
"""	

pygame.init();
pygame.display.set_mode((1,1));

motor1 = [17,27];
motor2 = [5,6];
motor3 = [23,24];
motors = [motor1,motor2,motor3];

io.setmode(io.BCM);
io.setup(motor1,io.OUT);
io.setup(motor2,io.OUT);
io.setup(motor3,io.OUT);

control.resetMotor(motors);

for motor in motors:
	control.motorForward(motor);

time.sleep(5);

for motor in motors:
	control.motorBackward(motor);
time.sleep(1);

control.allOff(motors);

active = True

while active:
	events = pygame.event.get()
	key = pygame.key.get_pressed()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				control.motorForward(motor1);
				print("Up") 
			if event.key == pygame.K_q:
				control.motorBackward(motor1);
				print("Down")
			if event.key == pygame.K_e:
				control.motorOff(motor1);
			if event.key == pygame.K_a:
				control.motorForward(motor2);
				print("Up") 
			if event.key == pygame.K_s:
				control.motorBackward(motor2);
				print("Down")
			if event.key == pygame.K_d:
				control.motorOff(motor2);
			if event.key == pygame.K_z:
				control.motorForward(motor3);
				print("Up") 
			if event.key == pygame.K_x:
				control.motorBackward(motor3);
				print("Down")
			if event.key == pygame.K_c:
				control.motorOff(motor3);
			if event.key == pygame.K_r:
				control.end(motors);
				active = False;
				print("End.")
				io.cleanup()
			if event.key == pygame.K_f:
				control.motorForward(motor2)
				speak("Hello")
				control.motorBackward(motor2)
				control.motorOff(motor2)
