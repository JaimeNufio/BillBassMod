import RPi.GPIO as io;

"""
Easier Ussage of these basic ideas for me.
"""

def initMotor(motorset):
    io.setwarnings(False);
    io.setmode(io.BCM);
    for motor in motorset:
    	io.setup(motor[1],io.OUT)
    	io.setup(motor[0],io.OUT)
        io.output(motor[1],0)
        io.output(motor[0],0)
        

    print("motors Init'd")
	
def motorForward(motor):

    io.setmode(io.BCM);
    io.output(motor[0],0)
    io.output(motor[1],1)
#    motorOff(motor)

def motorBackward(motor):
   
    io.setmode(io.BCM);
    io.output(motor[0],1)
    io.output(motor[1],0)
#    motorOff(motor)

def motorOff(motor):
    io.setmode(io.BCM)

def motorOff(motor):
    io.output(motor[0],0)
    io.output(motor[1],0)

def end(motors):
    io.setmode(io.BCM)
    for motor in motors:
        motorOff(motor)
#    io.cleanup()

    for motor in motors:
        motorOff(motor)
    io.cleanup()
    print("done!");
