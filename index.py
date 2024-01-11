import pygame
import sys
import math
from constants import *

pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)

animation_value = 0
rotation_multipler = 1

while True:
    animation_value += ROTATION_SPEED * rotation_multipler

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if e.type == pygame.MOUSEBUTTONDOWN:
            rotation_multipler *= -1

    pygame.draw.rect(window,(10,10,20), (0,0,SCREEN_SIZE[0],SCREEN_SIZE[1]))

    pygame.draw.circle(window, (100,130,200), 
                       (math.sin(animation_value) * 100 + SCREEN_SIZE[0]/2,
                        SCREEN_SIZE[1] - 50 + math.cos(animation_value) * 100)
                    , CIRCLE_RADIUS)
    
    pygame.draw.circle(window, (210,100,100), 
                       (-math.sin(animation_value) * 100 + SCREEN_SIZE[0]/2,
                        SCREEN_SIZE[1] - 50 - math.cos(animation_value) * 100)
                    , CIRCLE_RADIUS)

    pygame.display.update()