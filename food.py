import pygame, sys, random
from pygame.locals import *

WHITE = (255,255,255) #food color


class Food:
    #initialzies based on size of board which should be what it's called with.
    def __init__(self, xcoord, ycoord):
        self.pos = random.random()*(xcoord, ycoord)

    #returns position of food
    def get_pos(self):
        return self.pos
