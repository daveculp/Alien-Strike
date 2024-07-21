#!/usr/bin/env python

import random, pygame, sys, GameSprite
from Starfield2 import *

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700

pygame.init()
#init screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#clock to keep track of framerate
clock = pygame.time.Clock()

#List is passed in as [numstars, radius, velocity]
#Make a 4 layer parallax scrolled star field
star_field_struct =  [
    [900, 1, 1],
    [300, 2, 3],
    [50, 3, 6]
    ]
    
scroll_direction= SCROLL_TOP_BOTTOM

star_field = Starfield(SCREEN_WIDTH, SCREEN_HEIGHT, (0, SCREEN_WIDTH-4), (5, SCREEN_HEIGHT-5), star_field_struct, scroll_direction, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                scroll_direction += 1
                if scroll_direction > 4: scroll_direction = 1
                star_field.scroll_dir = scroll_direction
                

    star_field.update()
    screen.fill( (0,0,0) )
    star_field.draw(screen)
    pygame.display.update()

    clock.tick(30)
