import RPi.GPIO as io;
import MotorControl as control
import Speech as talky
import pygame
import time
import pyttsx
import thread

motor1 = [17,27];
motor2 = [5,6];
motor3 = [23,24];
motors = [motor1,motor2,motor3];	
pygame.init();
pygame.display.set_mode((1,1));
active = True;
count = 0;
delay = 250 ;  #150 is a bit fast

def startUpTest(tick):
	control.resetMotor(motors);
	for motor in motors:
		control.motorForward(motor);
	time.sleep(tick);
	for motor in motors:
		control.motorBackward(motor);
	time.sleep(tick);

startUpTest(.1);
control.allOff(motors);

def movementThread():
	global phase
	global active
	count = 1;
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
					control.motorOff(motor1);
				if event.key == pygame.K_e:
					control.motorOff(motor1);
				if event.key == pygame.K_a:		#Mouth
					control.motorForward(motor2);
					print("Up") 
				if event.key == pygame.K_s:		#Mouth
					control.motorBackward(motor2);
					print("Down")
					control.motorOff(motor2);
				if event.key == pygame.K_d:
					control.motorOff(motor2);
				if event.key == pygame.K_z:
					control.motorForward(motor3);
					print("Up") 
				if event.key == pygame.K_x:
					control.motorBackward(motor3);
					print("Down")
					control.motorOff(motor3);
				if event.key == pygame.K_c:
					control.motorOff(motor3);
				if event.key == pygame.K_r:
					control.end(motors);
					active = False;
					print("End.")
					io.cleanup()
				if event.key == pygame.K_f:
					print("Empty");
					#Speech Button
				if event.key == pygame.K_t:
					print("Talk Button");
					talky.speakWords("Hello World!");

def talker():
	count = 1;
	state = True;
	while active:
		if pygame.mixer.music.get_busy():
			state = True
			pygame.time.delay(delay);	
			print("talk: "+str(count));
			count*=-1;
			if (count > 0):
				control.motorForward(motor2);
			else:
				control.motorBackward(motor2);
		else:
			if state:
				control.motorOff(motor2);
				state = False;
								

thread.start_new_thread(movementThread,());
thread.start_new_thread(talker,());

while active:
	pass;
