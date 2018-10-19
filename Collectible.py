import pygame
import random

class Collectible:
    def __init__(self):
        self.loc_x, self.loc_y = random.randint(20,480), random.randint(20,480)
        self.height, self.width = 10,10
        self.exist_timer = 0

class GoodCollectible(Collectible):
    pass

class BadCollectible(Collectible):
    pass

class SpecialCollectible(Collectible):
    pass