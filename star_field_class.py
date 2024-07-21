#!/usr/bin/env python

import random, pygame, sys
from Starfield import *

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 900

pygame.init()
#init screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#clock to keep track of framerate
clock = pygame.time.Clock()

star_field = Starfield(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, far_num=400, mid_num=100, close_num=20)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    star_field.update()
        
    screen.fill( (0,0,0) )
    star_field.draw(screen)
        
    pygame.display.update()

    clock.tick(30)
