import pygame
import random

class Snake:
    def __init__(self):
        self.head_x, self.head_y = 500,500
        self.speed = 5
        self.direction = 'west'

    def move(self, direction):
        if direction == 'east':
            self.head_x += self.speed
        if direction == 'west':
            self.head_x -= self.speed
        if direction == 'north':
            self.head_y -= self.speed
        if direction == 'south':
            self.head_y += self.speed

