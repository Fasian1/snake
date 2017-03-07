import pygame, sys, random
WHITE = (255,255,255) #food color


class Food:
    #initialzies based on size of board which should be what it's called with.
    def __init__(self, xcoord, ycoord, width, snake_obj):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.width = width
        self.pos = [random.random()*xcoord/width, random.random()*ycoord/width]
        self.pos = [self.pos[0]*width, self.pos[1]*width]
        self.rectangle = pygame.Rect(self.pos, (width, width))
        while self.rectangle in snake_obj.tail.itervalues() or self.rectangle == snake_obj.head:
            self.random_food()


    def random_food(self):
        self.pos = [random.random() * self.xcoord / self.width, random.random() * self.ycoord / self.width]
        self.pos = [self.pos[0] * self.width, self.pos[1] * self.width]
        self.rectangle = pygame.Rect(self.pos, self.width, self.width)

    #returns position of food
    def get_pos(self):
        return self.pos

    def get_rect(self):
        return self.rectangle
