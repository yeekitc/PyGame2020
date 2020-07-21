import pygame
import random
import settings

#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitate")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

#Game loop
running = True
while running:
	#keep loop running at the right speed
	clock.tick(FPS)
	#process input (events)
	for event in pygame.event.get():
		#check for closing window
		if event.type == pygame.QUIT:
			running = False

# update
all_sprites.update()