import pygame
from constants import OB_COLOR, SCREEN_SIZE, LAYER_DISTANCE, LAYER_OFFSET, OB_SIZE

class OB:
    def __init__(self, layer, x):
        self.x = x
        self.layer = layer
        self.size = OB_SIZE

    def draw(self, window, ob_offset):
        y = SCREEN_SIZE[1] - self.size[1] - self.layer * LAYER_DISTANCE - LAYER_OFFSET - ob_offset
        pygame.draw.rect(window, OB_COLOR, (self.x,  y, self.size[0], self.size[1])) # for now just rectangles