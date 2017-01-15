import MotorControl as control
import pygame
import time

motor1 = [17,27];
motor2 = [5,6]
motor3 = [23,24]
motors = [motor1,motor2,motor3];
motorState = [False,False,False];

pygame.init()
pygame.display.set_mode((1,1))#screensize
running = True
active = True

control.initMotor(motors);

try:
    while active:
        time.sleep(1)
        tempMotorState = [False,False,False]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    tempMotorState[0]=True
                if event.key == pygame.K_w:
                    tempMotorState[0]=False
                if event.key == pygame.K_a:
                    tempMotorState[1]=True
                if event.key == pygame.K_s:
                    tempMotorState[1]=False
                if event.key == pygame.K_z:
                    tempMotorState[2]=True
                if event.key == pygame.K_x:
                    tempMotorState[2]=False
        print(tempMotorState);
        for i in range(len(tempMotorState)):
            if tempMotorState[i]:
                control.motorOn(motors[i]);
            else:
                control.motorOff(motors[i]);
            
                

except KeyboardInterrupt:
    pass

control.end(motors)

