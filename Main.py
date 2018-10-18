import pygame, time, sys, random
from GameWindow import GameWindow
from Snake import Snake

pygame.init()
window = GameWindow(800, 600)
snake = Snake()
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        snake.move('west')
    if pressed[pygame.K_RIGHT]:
        snake.move('east')
    if pressed[pygame.K_UP]:
        snake.move('north')
    if pressed[pygame.K_DOWN]:
        snake.move('south')

    window.draw_snake(snake)
    clock.tick(60)
