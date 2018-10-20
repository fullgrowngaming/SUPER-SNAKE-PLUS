import pygame

class Snake:
    def __init__(self):
        self.head = [500,500]
        self.segments = []
        self.segments.append(self.head)
        self.speed = 5
        self.height, self.width = 18,18
        self.direction = None
        self.score = 0

    def move(self):
        #update head
        if self.direction == 'east':
            self.head[0] += self.speed
        if self.direction == 'west':
            self.head[0] -= self.speed
        if self.direction == 'north':
            self.head[1] -= self.speed
        if self.direction == 'south':
            self.head[1] += self.speed

    def update_segments(self):
        #lol
        for index, segment in enumerate(self.segments):
            if index == 0:
                self.segments[index][0] = self.head[0]
                self.segments[index][1] = self.head[1]
            if index != 1:
                self.segments[index-1][0] = self.segments[index][0]
                self.segments[index-1][1] = self.segments[index][1]

    def lengthen(self):
        self.segments.append([self.head[0], self.head[1]])



