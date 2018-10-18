import pygame
import random

class Snake:
    def __init__(self):
        self.head_x, self.head_y = 500,500
        self.speed = 5
        self.height, self.width = 25,25
        self.direction = None
        self.moving = True
        self.score = 0

    def move(self):
        if self.direction == 'east':
            self.head_x += self.speed
        if self.direction == 'west':
            self.head_x -= self.speed
        if self.direction == 'north':
            self.head_y -= self.speed
        if self.direction == 'south':
            self.head_y += self.speed

