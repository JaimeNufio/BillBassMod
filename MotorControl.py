import RPi.GPIO as io;
import time;

def initMotor(motorset):
    io.setmode(io.BCM)
    for motor in motorset:
        for out in motor:
            io.setup(out,io.OUT)#initialize
            io.output(out,0) #turn off

def motorOn(motor):
    io.output(motor[0],1)
    io.output(motor[1],0)

def motorOff(motor):
    for out in motor:
        io.output(out,0)

def end(motors):
    for motor in motors:
        motorOff(motor)
    io.cleanup()
