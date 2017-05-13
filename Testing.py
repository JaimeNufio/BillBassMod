import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

on = [17,23,5]
off = [27,24,6]

GPIO.setup(on,GPIO.OUT)
GPIO.setup(off,GPIO.OUT)

mode = False

GPIO.output(17,mode)
GPIO.output(5,mode)
GPIO.output(23,mode)

GPIO.output(27,False)
GPIO.output(24,False)
GPIO.output(6,False)

