import pygame
from Snake import Snake

class GameWindow:
    '''Creates and maintains the game window'''
    white =       (255,255,255)
    black =       (0,0,0)
    red =         (255,0,0)
    green =       (0,255,0)
    blue =        (0,0,255)

    def __init__(self, window_res_x, window_res_y):
        self.window_res_x = window_res_x
        self.window_res_y = window_res_y
        self.window = pygame.display.set_mode((window_res_x, window_res_y))
        self.window.fill(GameWindow.white)
        pygame.display.set_caption('SUPER SNAKE PLUS')
        self.display()

    def display(self):
        pygame.display.update()

    def draw_snake(self, Snake):
        self.window.fill(GameWindow.white)
        pygame.draw.rect(self.window, GameWindow.green, [Snake.head_x, Snake.head_y, 25, 25])
        self.display()

    def display_text(self, msg, color, pos_x, pos_y):
        text = self.font.render(msg, True, GameWindow.red)
        self.window.blit(text, [pos_x, pos_y])
        self.display()