import pygame
from constants import OB_COLOR, SCREEN_SIZE, LAYER_DISTANCE, LAYER_OFFSET, OB_SIZE, CIRCLE_RADIUS
from utils import dis_point_from_line_by_points

# spawning obs
POSES = (20, SCREEN_SIZE[0] / 2 - OB_SIZE[0] / 2, SCREEN_SIZE[0] - 20 - OB_SIZE[0])

class OB:
    def __init__(self, layer, place_index):
        self.x = POSES[place_index]
        self.place_index = place_index

        self.layer = layer
        self.size = OB_SIZE

        self.place_index = place_index

        self.collided = False

    def draw(self, window, ob_offset):
        y = SCREEN_SIZE[1] - self.size[1] - self.layer * LAYER_DISTANCE - LAYER_OFFSET - ob_offset
        pygame.draw.rect(window, OB_COLOR if not self.collided else (200, 100, 100), (self.x,  y, self.size[0], self.size[1])) # for now just rectangles

    def check_collision(self, player_pos, ob_offset): # here we will use the second way mentioned
        # checking for pos to make sure only needed data is generated
        Y = 0
        for player in player_pos:
            X = self.x
            Y = SCREEN_SIZE[1] - self.size[1] - self.layer * LAYER_DISTANCE - LAYER_OFFSET - ob_offset

            bottom_right = (X + self.size[0], Y + self.size[1])
            bottom_left = (X, Y + self.size[1])
            top_right = (X + self.size[0], Y) if self.place_index == 0 or self.place_index == 1 else None
            top_left = (X, Y) if self.place_index == 2 or self.place_index == 1 else None

            d = None

            if Y < player[1] < Y + self.size[1]: # ball is in between
                if self.place_index == 0: # the ob on the left side
                    d = dis_point_from_line_by_points(top_right, bottom_right, player)
                    
                elif self.place_index == 1: # the ob on the middle spot
                    if player[0] < X: # on the right side of the ob
                        d = dis_point_from_line_by_points(top_left, bottom_left, player)
                    elif player[0] > X + self.size[0]: # on the left side of the ob
                        d = dis_point_from_line_by_points(top_right, bottom_right, player)

                elif self.place_index == 2:
                    d = dis_point_from_line_by_points(top_left, bottom_right, player)


            elif X < player[0] < X + self.size[0]: # ball is under
                d = dis_point_from_line_by_points(bottom_left, bottom_right, player)

            if d and d < CIRCLE_RADIUS - 10 and not self.collided:
                self.collided = True
                return Y, True

        return Y, False