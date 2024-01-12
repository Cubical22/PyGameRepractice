import pygame
import sys
from constants import *
from Items.OB.OB import OB

import Items.Player as Player

# pygame setup
pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)

# variables used for the moving ball animatio
animation_value = 0
rotation_multipler = 1

# spawning obs
OBS.extend([
    OB(0,20),
    OB(1,20),
    OB(2,20),
    OB(3,20),
    OB(4,20),
    OB(5,20),
])
ob_offset = 0

# main game loop
while True:
    # updating the animation value based on the rotation multiplier
    # basically the multiplier just reversed the movement when clicked
    animation_value += ROTATION_SPEED * rotation_multipler

    # value used to move the OBs based on layers
    ob_offset -= ROTATION_SPEED * 57

    for e in pygame.event.get(): # event handling
        if e.type == pygame.QUIT: # exit event
            pygame.quit()
            sys.exit(0)
        if e.type == pygame.MOUSEBUTTONDOWN: # reverse uppon click
            rotation_multipler *= -1

    # clearing the view with a color
    pygame.draw.rect(window,(10,10,20), (0,0,SCREEN_SIZE[0],SCREEN_SIZE[1]))

    # drawing the player balls (will be moved later)
    Player.draw_player(window, animation_value)

    # drawing OBs
    for ob in OBS:
        ob.draw(window, ob_offset)

    pygame.display.update() # updating the display