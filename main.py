import pygame
from pygame.locals import *
import sys
import os

def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

import settings

os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Gravitate")


bkgd = pygame.image.load("bkgd600.png").convert()
x = 0 # background position

# main loop
while True:
	events()
	relativeX = x % bkgd.get_rect().width
	DS.blit(bkgd, (relativeX - bkgd.get_rect().width, 0))

	if relativeX < W:
		DS.blit(bkgd, (relativeX, 0))

	x -= 1 #bkgd moves left


	pygame.display.update()
	CLOCK.tick(FPS)


