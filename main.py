import pygame, sys
from pygame.locals import *
import snake
import food

pygame.init()
FPS = 15
FPSCLOCK = pygame.time.Clock()

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
snake_obj = snake.Snake(XLEN, YLEN, WIDTH)
food_obj = food.Food(XLEN, YLEN, WIDTH, snake_obj)

def main():
    global food_obj, snake_obj
    while True:  #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                snake_obj.move(event)
            # if event.key == K_ESCAPE:
            #     terminate()
            game_state = snake_obj.update(food_obj)
            if game_state == -1:
                return #Game Over!
            elif game_state:
                food_obj = food.Food(XLEN, YLEN)
        draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def draw():
    pygame.draw.rect(DISPLAYSURF, RED, snake_obj.head)
    for segment in snake_obj.tail:
        pygame.draw.rect(DISPLAYSURF, WHITE, segment)
    pygame.draw.rect(DISPLAYSURF, WHITE, food_obj.get_rect())

if __name__ == '__main__':
    main()