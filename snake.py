import pygame, sys
from pygame.locals import *
import food
from Queue import *
import main

#colors
WHITE = (255,255,255) #snake and food 
RED = (255,0,0) #head


class Snake:
    def __init__(self, xcoord, ycoord, width):
        self.x = (xcoord - self.width)/2
        self.y = (ycoord + self.width)/2 #these two are useless...atm.
        self.width = width
        # makes a square in the center of the screen
        self.head = pygame.Rect(self.x, self.y, self.width, self.width)
        self.tail = []
        self.velocity = (0, 0)
        self.pos = (self.x, self.y)

    #returns position of head of snake
    def get_pos(self):
        return self.head.center

    #returns velocity
    def get_velocity(self):
        return self.velocity

    #determines direction the snake moves based on user input.
    #do not let user move 180 from current velocity.
    def move(self, action):
        # if action == pygame.K_LEFT:
        #   self.head.move((-self.velocity,0))
        # elif action == pygame.K_RIGHT:
        #   self.head.move((self.velocity,0))
        # elif action == pygame.K_UP:
        #   self.head.move((0,-self.velocity))
        # elif action == pygame.K_DOWN:
        #   self.head.move((0,self.velocity))
        if action == pygame.K_LEFT and self.velocity != (self.width, 0):
            self.velocity = (-self.width, 0)
        elif action == pygame.K_RIGHT and self.velocity != (-self.width, 0):
            self.velocity = (self.width, 0)
        elif action == pygame.K_UP and self.velocity != (0, self.width):
            self.velocity = (0, -self.width)
        elif action == pygame.K_DOWN  and self.velocity != (0, -self.width):
            self.velocity = (0, self.width)

    #updates the snake's positions. Returns -1 if the snake dies. Otherwise returns True if the snake ate the food.
    def update(self, food):
        self.head.move(self.velocity)
        #self.head.move(self.velocity[0], self.velocity[1])
        for segment in self.tail:
            segment.move(self.velocity)
            #segment.move(self.velocity[0], self.velocity[1])
        if self.head.collidelist(self.tail) or self.x >= main.XLEN :
            return -1
        ate_food = self.head.collidepoint(food.get_pos())
        new_tail_rect = pygame.Rect(self.get_pos(), (self.width, self.width))
        self.tail.append(new_tail_rect)
        if not ate_food:
            self.tail.get()
        return ate_food
