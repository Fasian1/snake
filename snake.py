import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30 
fpsClock = pygame.time.Clock()

#setting up the window
DISPLAYSURF = pygame.display.set_mode((400,300)) #sets width and heigh of window to 400,300 respectively
pygame.display.set_caption('It\'s A Snake! ...Game.')

#set up colors
BLACK = (0,0,0) #background
WHITE = (255,255,255) #snake and food 
RED = (255,0,0) #head

while True: #main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
