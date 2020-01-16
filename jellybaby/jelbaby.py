from gpiozero import Button
import pygame
from time import sleep

pygame.init()
pygame.mixer.init()

jelly = Button(3)
burp =  pygame.mixer.Sound('burp.wav')


while True:
	jelly.wait_for_press()
	burp.play()
	sleep(2)
	burp.stop()




