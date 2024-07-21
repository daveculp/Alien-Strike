#!/usr/bin/env python

import random, pygame, sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900

far_field_pos = list()
far_field_color = list()
far_field_vel = 1

middle_field_pos= list()
middle_field_color = list()
middle_field_vel = 3

close_field_pos = list()
close_field_color = list()
close_field_vel = 6
    

#generate far field
for x in range(0, 50):
    point = [random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT) ]
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255) )
    far_field_pos.append(point)
    far_field_color.append(color)

#generate med field
for x in range(0, 25):
    point = [random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT) ]
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255) )
    middle_field_pos.append(point)
    middle_field_color.append(color)

#generate close field
for x in range(0, 20):
    point = [random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT) ]
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255) )
    close_field_pos.append(point)
    close_field_color.append(color)
    

pygame.init()
#init screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#clock to keep track of framerate
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    #move far_field
    for num in range(0, len(far_field_pos) ):
        y=far_field_pos[num][1]
        y+=1
        if y>=SCREEN_HEIGHT: y = (SCREEN_HEIGHT-y)
        far_field_pos[num][1] = y
        
    #move med_field
    for num in range(0, len(middle_field_pos) ):
        y=middle_field_pos[num][1]  
        y+=3
        if y>=SCREEN_HEIGHT: y = (SCREEN_HEIGHT-y)
        middle_field_pos[num][1] = y
        
    #move med_field
    for num in range(0, len(close_field_pos) ):
        y=close_field_pos[num][1]
        y+=6
        if y>=SCREEN_HEIGHT: y = (SCREEN_HEIGHT-y)
        close_field_pos[num][1] = y

    screen.fill( (0,0,0) )
    for pos,color in zip(far_field_pos, far_field_color):
        #pygame.draw.rect(screen, color, (pos[0],pos[1],1,1), 0)
        screen.set_at( (pos[0],pos[1]), color )
        
        
    for pos,color in zip(middle_field_pos, middle_field_color):
        pygame.draw.circle(screen, color, (pos[0],pos[1]),2, 0)
        
    for pos,color in zip(close_field_pos, middle_field_color):
        pygame.draw.circle(screen, color, (pos[0],pos[1]),3, 0)
        
    pygame.display.update()

    clock.tick(30)
