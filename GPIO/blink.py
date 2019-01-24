import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
LED = 11
i = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
while i<10:
	GPIO.output(LED,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(LED,GPIO.LOW)
	time.sleep(1)
	i = i+1
GPIO.output(LED,GPIO.LOW)
