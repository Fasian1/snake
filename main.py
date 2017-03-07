import pygame, sys
from pygame.locals import *
import snake
import food

pygame.init()
FPS = 30 
fpsClock = pygame.time.Clock()

#setting up the window
XLEN = 400
YLEN = 400
DISPLAYSURF = pygame.display.set_mode((XLEN, YLEN))  #sets width and heigh of window to 400,300 respectively
pygame.display.set_caption('It\'s A Snake! ...Game.')
WIDTH = 20

#set up colors
BLACK = (0, 0, 0)  #background
WHITE = (255, 255, 255)  #snake and food
RED = (255, 0, 0)  #head

#intializing snake
snake = snake.Snake(XLEN, YLEN, WIDTH)
food = food.Food(XLEN, YLEN)

while True:  #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        snake.move(event)
    pygame.display.update()
