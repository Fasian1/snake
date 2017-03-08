import pygame, sys
from pygame.locals import *
import food
from Queue import *

#colors
WHITE = (255,255,255) #snake and food 
RED = (255,0,0) #head


class Snake:
    def __init__(self, xcoord, ycoord, width):
        self.XLEN = xcoord
        self.YLEN = ycoord
        self.x = (xcoord - width)/2
        self.y = (ycoord + width)/2 #these two are useless...atm.
        self.width = width
        # makes a square in the center of the screen
        self.head = pygame.Rect(self.x, self.y, self.width, self.width)
        self.tail = {}
        self.velocity = (0, 0)
        self.pos = (self.x, self.y)
        self.counter = 0

    #returns position of head of snake. Top left of rectangle.
    def get_pos(self):
        return self.head.topleft

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
        if action.key == pygame.K_LEFT and self.velocity != (self.width, 0):
            self.velocity = (-self.width, 0)
        elif action.key == pygame.K_RIGHT and self.velocity != (-self.width, 0):
            self.velocity = (self.width, 0)
        elif action.key == pygame.K_UP and self.velocity != (0, self.width):
            self.velocity = (0, -self.width)
        elif action.key == pygame.K_DOWN  and self.velocity != (0, -self.width):
            self.velocity = (0, self.width)

    #updates snake's positions. Returns -1 if the snake dies. Otherwise returns True if snake ate food false otherwise.
    def update(self, food_pellet):
        #moving the snake. Head first then tail.
        new_tail_rect = pygame.Rect(self.get_pos(), (self.width, self.width))
        self.head = self.head.move(self.velocity)
        #check for death by wall or hitting the tail.
        if (self.head.right > self.XLEN or
                self.head.left < 0 or self.head.bottom > self.YLEN or self.head.top < 0):
            return -1
        collide = False
        for segment in self.tail:
            if self.head.colliderect(self.tail[segment]):
                collide = True
        if collide:
            return -1
        ate_food = self.head.collidepoint(food_pellet.get_pos())
        self.counter += 1
        self.tail[self.counter] = new_tail_rect
        if len(self.tail.keys()) == 0:
            return ate_food
        if ate_food:
            return ate_food
        last = min(self.tail.keys())
        del self.tail[last]
            # for segment in self.tail:
            #     self.tail[segment] = self.tail[segment].move(self.velocity)
                # segment.move(self.velocity)
                # segment.move(self.velocity[0], self.velocity[1])
        return ate_food
