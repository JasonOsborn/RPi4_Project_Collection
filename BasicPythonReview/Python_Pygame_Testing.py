import pygame
from pygame.locals import *
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen = pygame.display.set_mode((width,height))

# imageEX = pygame.image.load('imageExName.png')
    # Load an image into memory
# imageEx = pygame.transform.scale(imageEx, (width,height))
    # Redefine image as scaled image
# screen.blit(imageEx, (0,0))
    # Load image onto screen

pygame.display.update()

sleep(.03)
# delay in sec

# soundEx = pygame.mixer.Sound('soundExName.wav')
# soundEx.play()
# soundEx.stop()

pygame.quit()
