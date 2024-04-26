import pygame
import sys
from constants import *
from Items.OB.OB import OB

import Items.Player as Player

# pygame setup
pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)

# variables used for the moving ball animation
animation_value = 0
rotation_multiplier = 1

# 0: left 1: middle 2: right
OBS.extend([
    OB(0, 0),
    OB(1, 2),
    OB(2, 1),
    OB(3, 2),
    OB(4, 0),
    OB(5, 1),
    OB(6, 2),
    OB(7, 2),
])
ob_offset = 0

# main game loop
while True:
    # updating the animation value based on the rotation multiplier
    # basically the multiplier just reversed the movement when clicked
    animation_value += ROTATION_SPEED * rotation_multiplier * LAYER_DISTANCE / LAYER_FACTOR_DEVIDER

    # value used to move the OBs based on layers
    ob_offset -= ROTATION_SPEED * 57 * LAYER_DISTANCE / LAYER_FACTOR_DEVIDER

    for e in pygame.event.get(): # event handling
        if e.type == pygame.QUIT: # exit event
            pygame.quit()
            sys.exit(0)
        if e.type == pygame.MOUSEBUTTONDOWN: # reverse uppon click
            rotation_multiplier *= -1

    # clearing the view with a color
    pygame.draw.rect(window,(10,10,20), (0,0,SCREEN_SIZE[0],SCREEN_SIZE[1]))

    # drawing the player balls (will be moved later)
    player_coordinates = Player.draw_player(window, animation_value)
    # blue & red
    # ((X1, Y1),(X2, Y2))

    # drawing OBs
    for ob in OBS: 
        # plan is to check for collision inside the ob class
        # since great amount of data needed is already inside the ob class
        ob.draw(window, ob_offset) # (x, y)
        ob.check_collision(player_coordinates, ob_offset)

    pygame.display.update() # updating the display