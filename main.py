import pygame
from pygame.locals import *
import os
import sys
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 534
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gravitate')

bkgd = pygame.image.load('SCIFI-2.png').convert()
bkgdX = 0
bkgdX2 = bkgd.get_width()

clock = pygame.time.Clock()

class player(object):
	run = [pygame.transform.rotozoom(pygame.image.load(os.path.join('Sprite', 'Run', str(x) + '.png')), 0, 2.5) for x in range(1,16)]
	jump = [pygame.transform.rotozoom(pygame.image.load(os.path.join('Sprite', 'Walk', str(x) + '.png')), 0, 2.5) for x in range(1,13)]
	fall = [pygame.transform.rotozoom(pygame.image.load(os.path.join('Sprite', 'Death', 'Character_01_Death_' + str(x) + '.png')), 0, 2.5) for x in range (1,17)]
	blank = pygame.transform.rotozoom(pygame.image.load(os.path.join('Sprite','blank.png')), 0, 2.5)
	
	#jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,]

	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.jumping = False
		self.jumpCount = 0
		self.runCount = 0
		self.falling = False
		self.fallCount = 0
		self.fallFrame = 0

	def draw(self, win):
		if self.jumping:
			window.blit(self.jump[self.jumpCount//18], (self.x, self.y))
			if self.jumpCount > 108:
				self.jumpCount = 0
			if self.y < 80 and self.jumpCount < 100:
				self.y += 1
			else:
				self.y = 80
			#self.jumpList[self.jumpCount] * 1.2
			self.jumpCount += 1
			self.hitbox = (self.x + 50, self.y + 50, self.width-24, self.height-5)
			#	self.jumping = False
			#	self.runCount = 0

		elif self.falling:
			
			if self.fallFrame % 10 <= 4:
				if self.fallCount < 160:
					window.blit(self.fall[self.fallCount//10], (self.x, self.y))
					self.fallCount += 1
					
				if self.fallCount >= 160:
					window.blit(self.fall[15],(self.x, self.y))

			elif self.fallFrame%10 <= 9:
				window.blit(self.blank, (self.x, self.y))

			#else:
				
			#if self.fallCount > 200:
			#	self.falling = False
			#self.jumpList[self.jumpCount] * 1.2
			self.fallFrame += 1
			#self.hitbox = (self.x + 50, self.y + 50, self.width-24, self.height-5)
			#	self.jumping = False
			#	self.runCount = 0
			#window.blit(self.fall[0], (self.x, self.y + 30))

		else:
			if self.y > 285 and self.runCount < 100:
				self.y -= 1
			else:
				self.y = 285
			if self.runCount > 42:
				self.runCount = 0
			window.blit(self.run[self.runCount//6], (self.x,self.y))
			self.runCount += 1
			self.hitbox = (self.x + 50, self.y + 50, self.width - 24, self.height - 5)
		pygame.draw.rect(window, (255,0,0), self.hitbox, 2)

class enemy(object):
	img = pygame.transform.rotozoom(pygame.image.load(os.path.join('Obstacle', 'triangle' + '.png')), 0, 0.1)
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hitbox = (x,y,width,height)
		self.count = 0
	
	def draw(self,window):
		self.hitbox = (self.x + 20, self.y + 15, self.width - 15, self.height - 5)
		if self.count >= 8:
			self.count = 0
		window.blit(self.img, (self.x,self.y))

		self.count += 1
		pygame.draw.rect(window, (255,0,0), self.hitbox, 2)

	def collide(self, rect):
		if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
			if rect[1] + rect[3] > self.hitbox[1]:
				return True
		else:
			return False

class enemyTop(object):
	img = pygame.transform.rotozoom(pygame.image.load(os.path.join('Obstacle', 'triangle' + '.png')), 180, 0.1)
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hitbox = (x,y,width,height)
		self.count = 0
	
	def draw(self,window):
		self.hitbox = (self.x + 20, self.y + 15, self.width - 15, self.height - 5)
		if self.count >= 8:
			self.count = 0
		window.blit(self.img, (self.x,self.y))

		self.count += 1
		pygame.draw.rect(window, (255,0,0), self.hitbox, 2)

	def collide(self, runner):
		if (runner[0] + runner[2] > self.hitbox[0]) and (runner[0] < self.hitbox[0] + self.hitbox[2]):
			if runner[1] + runner[3] > self.hitbox[1] and runner[1] < self.hitbox[1] + self.hitbox[3]:
			#if runner[1] + runner[3] > self.hitbox[1]:
				#runner.jumping = False
				return True
			#else:
			#	return False
		else:
			return False

		#if runner[0] + runner[2] > self.hitbox[0] and runner[0] < #self.hitbox[0] + self.hitbox[2]:
		#	if runner[1] + 5 <= self.hitbox[1] + self.hitbox[3]:
			#if runner[1] + 5 >= self.hitbox[1] and runner[1] + 5 < self.hitbox[1] + self.hitbox[3]:
			
		#		return True
		#else:
		#	return False



def redrawWindow():
	window.blit(bkgd, (bkgdX, 0))
	window.blit(bkgd, (bkgdX2, 0))
	runner.draw(window)
	for objectt in objects:
		objectt.draw(window)
	pygame.display.update()

def reset():
	pass


runner = player(50, 285, 64, 64)
pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, random.randrange(3000,5000)) #this event generates at random intervals - between 3 and 5 seconds
speed = 30
run = True

objects = []

while run:
	#redrawWindow()
	slowCount = 0

	for objectt in objects:
		if objectt.collide(runner.hitbox):
			runner.falling = True
			runner.jumping = False
		
		if objectt.x < -32:
			objects.pop(objects.index(objectt))
		
		else:
			objectt.x -= 1.4
	
	#if runner.falling == True:
		#if speed > 0:
		#	speed = speed - 50
		#speed = 0
		#slowCount += 1

	bkgdX -= 1.4
	bkgdX2 -= 1.4
	if bkgdX < bkgd.get_width() * -1:
		bkgdX = bkgd.get_width()
	if bkgdX2 < bkgd.get_width() * -1:
		bkgdX2 = bkgd.get_width()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()
		if event.type == USEREVENT+1:
			speed += 50
		if event.type == USEREVENT+2: #when the event generates...
			r = random.randrange(0,2) #randomly generate a number in the range 0-1 (2 is excluded)
			if r == 0: #if the randomly generated number is 0
				objects.append(enemy(810, 340, 64, 64)) #place a spike at the bottom
			else: #(if number is 1)
				objects.append(enemyTop(810, 120, 64, 64)) #place spike at the top

	keys = pygame.key.get_pressed()

	if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
		if not(runner.jumping):
			runner.jumping = True
	
	if keys[pygame.K_DOWN]:
		if(runner.jumping):
			runner.jumping = False

	clock.tick(speed)
	redrawWindow()