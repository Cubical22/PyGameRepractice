import pygame
from constants import OB_COLOR, SCREEN_SIZE, LAYER_DISTANCE, LAYER_OFFSET, OB_SIZE

# spawning obs
POSES = (20, SCREEN_SIZE[0] - 20 - OB_SIZE[0], SCREEN_SIZE[0] / 2 - OB_SIZE[0] / 2)

class OB:
    def __init__(self, layer, place_index):
        self.x = POSES[place_index]
        self.layer = layer
        self.size = OB_SIZE

        self.place_index = place_index

    def draw(self, window, ob_offset):
        y = SCREEN_SIZE[1] - self.size[1] - self.layer * LAYER_DISTANCE - LAYER_OFFSET - ob_offset
        pygame.draw.rect(window, OB_COLOR, (self.x,  y, self.size[0], self.size[1])) # for now just rectangles

    def check_collision(self, player_pos, ob_offset): # here we will use the second way mentioned
        # checking for pos to make sure only needed data is generated
        X = self.x
        Y = SCREEN_SIZE[1] - self.size[1] - self.layer * LAYER_DISTANCE - LAYER_OFFSET - ob_offset

        bottom_right = (X + self.size[0], Y + self.size[1])
        bottom_left = (X, Y + self.size[1])

        # !!! might need some adjustments
        if self.place_index == 0: # left side
            top_right = (X + self.size[0], Y)
            # ...
        elif self.place_index == 1: # middle side
            top_right = (X + self.size[0], Y)
            top_left = (X, Y)
            # ...
        elif self.place_index == 2: # right side
            top_left = (X, Y)