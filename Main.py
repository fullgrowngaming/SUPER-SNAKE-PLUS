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

    if pressed[pygame.K_LEFT] and snake.head_x > 0:
        snake.move('west')
    if pressed[pygame.K_RIGHT] and snake.head_x < window.res_x - snake.width:
        snake.move('east')
    if pressed[pygame.K_UP] and snake.head_y > 0:
        snake.move('north')
    if pressed[pygame.K_DOWN] and snake.head_y < window.res_y - snake.height:
        snake.move('south')

    window.draw_snake(snake)
    clock.tick(60)
