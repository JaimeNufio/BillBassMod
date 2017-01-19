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
    control.motorOn(motor1);
        
except KeyboardInterrupt:
    pass

control.end(motors)

"""
    while active:
        time.sleep(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    control.motorOn(motors[0]);
                if event.key == pygame.K_w:
                    control.motorOff(motors[0]);
                if event.key == pygame.K_a:
                    control.motorOn(motors[1]);
                if event.key == pygame.K_s:
                    control.motorOff(motors[1]);
                if event.key == pygame.K_z:
                    control.motorOn(motors[2]);
                if event.key == pygame.K_x:
                    control.motorOff(motors[2]);
"""
