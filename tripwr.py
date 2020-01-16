from gpiozero import LightSensor
from pygame import mixer
from picamera import PiCamera 


cam = PiCamera()
cam.rotation = 180
mixer.init()
snsr = LightSensor(4)
alert = mixer.Sound('tacNuke.wav')

while True:
	snsr.wait_for_dark()
	print('INTRUDER ALERT')
	alert.play()
	cam.capture('intruder.jpg')

