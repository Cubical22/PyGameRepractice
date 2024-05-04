import pygame
from constants import CIRCLE_RADIUS, SCREEN_SIZE
import math

def draw_player(window,animation_value):
    X1 = math.sin(animation_value) * 100 + SCREEN_SIZE[0]/2
    Y1 = SCREEN_SIZE[1] - 50 + math.cos(animation_value) * 100
    pygame.draw.circle(window, (80, 136, 87), 
                       (X1, Y1), CIRCLE_RADIUS)
    
    X2 = -math.sin(animation_value) * 100 + SCREEN_SIZE[0]/2
    Y2 = SCREEN_SIZE[1] - 50 - math.cos(animation_value) * 100
    pygame.draw.circle(window, (180, 192, 137), 
                       (X2, Y2), CIRCLE_RADIUS)

    return (X1, Y1),(X2, Y2)