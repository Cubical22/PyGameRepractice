import pygame
import sys
import math
from constants import *

# pygame setup
pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)

# variables used for the moving ball animatio
animation_value = 0
rotation_multipler = 1

# main game loop
while True:
    # updating the animation value based on the rotation multiplier
    # basically the multiplier just reversed the movement when clicked
    animation_value += ROTATION_SPEED * rotation_multipler

    for e in pygame.event.get(): # event handling
        if e.type == pygame.QUIT: # exit event
            pygame.quit()
            sys.exit(0)
        if e.type == pygame.MOUSEBUTTONDOWN: # reverse uppon click
            rotation_multipler *= -1

    # clearing the view with a color
    pygame.draw.rect(window,(10,10,20), (0,0,SCREEN_SIZE[0],SCREEN_SIZE[1]))

    # drawing the player balls (will be moved later)
    pygame.draw.circle(window, (100,130,200), 
                       (math.sin(animation_value) * 100 + SCREEN_SIZE[0]/2,
                        SCREEN_SIZE[1] - 50 + math.cos(animation_value) * 100)
                    , CIRCLE_RADIUS)
    
    pygame.draw.circle(window, (210,100,100), 
                       (-math.sin(animation_value) * 100 + SCREEN_SIZE[0]/2,
                        SCREEN_SIZE[1] - 50 - math.cos(animation_value) * 100)
                    , CIRCLE_RADIUS)

    pygame.display.update() # updating the display