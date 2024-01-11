import pygame
from constants import CIRCLE_RADIUS, SCREEN_SIZE
import math

def draw_player(window,animation_value):
    pygame.draw.circle(window, (100,130,200), 
                       (math.sin(animation_value) * 100 + SCREEN_SIZE[0]/2,
                        SCREEN_SIZE[1] - 50 + math.cos(animation_value) * 100)
                    , CIRCLE_RADIUS)
    
    pygame.draw.circle(window, (210,100,100), 
                       (-math.sin(animation_value) * 100 + SCREEN_SIZE[0]/2,
                        SCREEN_SIZE[1] - 50 - math.cos(animation_value) * 100)
                    , CIRCLE_RADIUS)