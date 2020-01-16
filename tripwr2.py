from gpiozero import LightSensor
from pygame import mixer
from picamera import PiCamera 
from time import sleep

cam = PiCamera()
cam.rotation = 180
mixer.init()
snsr = LightSensor(4)
alert = mixer.Sound('tacNuke.wav')

def alert():
	print('INTRUDER ALERT')
	alert.play()
	cam.capture('intruder.jpg')
	sleep(6)
	alert.stop()


while True:
	snsr.when_dark() = alert()
	

