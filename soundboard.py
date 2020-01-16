import pygame
from gpiozero import Button, LED
from time import sleep

pygame.init()
pygame.mixer.init()

##Non-optimized code

# work = pygame.mixer.Sound('work it.wav')
# make = pygame.mixer.Sound('make it.wav')
# doit = pygame.mixer.Sound('do it.wav')
# mix = pygame.mixer.Sound('makes us.wav') #I know it's actually "makes"

# #initialize buttons and LEDs
btnB = Button(2) 
# ledB = LED(2)

btnR = Button(3)
# ledR = LED(3)

btnG = Button(4)
# ledG = LED(4)

btnY = Button(17)
# ledY = LED(17)

#store LEDs into array, as to tie them with the buttons later
lights = [LED(27), LED(18), LED(22), LED(23)] 

ledB = LED(27)
ledR = LED(22)
ledG = LED(23)
ledY = LED(24)


btn_sounds = {
		btnB: [pygame.mixer.Sound('harder2.wav'), ledB], 
		btnR: [pygame.mixer.Sound('better2.wav'), ledR],
		btnG: [pygame.mixer.Sound('faster2.wav'),  ledG],
		btnY: [pygame.mixer.Sound('stronger2.wav'), ledY]
} 


def effects(fx):
	fx[0].play
	fx[1].blink


def Main():
	while True:
		for button, fx in btn_sounds.items():
			button.when_pressed = effects(fx)
			
            			
if __name__ == '__main__':
	Main()
