import pygame
from Snake import Snake

class GameWindow:
    '''Creates and maintains the game window'''
    white =       (255,255,255)
    black = (0,0,0)
    red   = (255,0,0)
    green = (0,255,0)
    blue  = (0,0,255)
    font  = pygame.font.SysFont(None, 25)

    def __init__(self, window_res_x, window_res_y):
        self.res_x = window_res_x
        self.res_y = window_res_y
        self.window = pygame.display.set_mode((window_res_x, window_res_y))
        self.window.fill(GameWindow.white)
        pygame.display.set_caption('SUPER SNAKE PLUS')
        self.display()

    def display(self):
        pygame.display.update()

    def draw_snake(self, Snake):
        pygame.draw.rect(self.window, GameWindow.green, [Snake.head[0], Snake.head[1], Snake.height, Snake.width])
        print(Snake.segments)
        for segment in Snake.segments:
            pygame.draw.rect(self.window, GameWindow.green,[segment[0], segment[1], Snake.height, Snake.width])

    def draw_collectible(self, Collectible):
        pygame.draw.rect(self.window, GameWindow.red, [Collectible.loc_x, Collectible.loc_y,
                                                       Collectible.height, Collectible.width])

    def display_text(self, msg, color, pos_x, pos_y):
        text = GameWindow.font.render(str(msg), True, GameWindow.red)
        self.window.blit(text, [pos_x, pos_y])