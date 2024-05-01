from constants import MAX_HEART_COUNT
import pygame

class State_manager:
    heart_count = 0
    score = 0

    def __init__(self):
        self.heart_count = MAX_HEART_COUNT # number of lives you have
        self.score = 0 # your current score

    def collided(self): # activated when collision happens
        self.heart_count -= 1

        if self.heart_count < 0:
            print("lost")

    def update_score(self):
        print(f'\rDodge the walls! ⭐ score: {self.score} ⭐ heart(s): {self.heart_count} ⭐                ', end="")