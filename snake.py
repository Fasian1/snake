import pygame, sys
from pygame.locals import *

#colors
WHITE = (255,255,255) #snake and food 
RED = (255,0,0) #head

class snake():
	def __init__(self, xcoord, ycoord):
		self.x = xcoord/2
		self.y = ycoord/2
		self.width = 20
		self.head = pygame.Rect(self.x-self.width/2, self.y + self.width/2, self.width, self.width) #makes a square in the center of the screen
		self.tail = []
		self.velocity = (0,0)
		self.pos = (self.x, self.y)

	#returns position of head of snake
	def get_pos(self):
		return (self.x, self.y)

	#returns velocity
	def get_velocity(self):
		return self.velocity

	#determines direction the snake moves
	def move(self, action):
		# if action == pygame.K_LEFT:
		# 	self.head.move((-self.velocity,0))
		# elif action == pygame.K_RIGHT:
		# 	self.head.move((self.velocity,0))
		# elif action == pygame.K_UP:
		# 	self.head.move((0,-self.velocity))
		# elif action == pygame.K_DOWN:
		# 	self.head.move((0,self.velocity))
		if action == pygame.K_LEFT:
			self.velocity = (-self.width,0)
		elif action == pygame.K_RIGHT:
			self.velocity = (self.width,0)
		elif action == pygame.K_UP:
			self.velocity = (0, -self.width)
		elif action == pygame.K_DOWN:
			self.velocity = (0, self.width)		

	#updates the snake's positions. 
	def update(self, food_pos):
		if self.head.collidepoint(food_pos):
			self.append.tail()