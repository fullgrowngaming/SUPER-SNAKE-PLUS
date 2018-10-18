import pygame, time, sys, random
pygame.init()
from GameWindow import GameWindow
from Snake import Snake


if __name__ == "__main__":
    window = GameWindow(800, 600)
    snake = Snake()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #handles keypresses and moving the snake
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            snake.direction = 'west'
        elif pressed[pygame.K_RIGHT]:
            snake.direction = 'east'
        elif pressed[pygame.K_UP]:
            snake.direction = 'north'
        elif pressed[pygame.K_DOWN]:
            snake.direction = 'south'

        snake.move()

        #handles screen boundaries
        if snake.head_x < 0:
            snake.head_x = 0
        if snake.head_x > window.res_x - snake.width:
            snake.head_x = window.res_x - snake.width
        if snake.head_y < 0:
            snake.head_y = 0
        if snake.head_y > window.res_y - snake.height:
            snake.head_y = window.res_y - snake.height

        window.draw_snake(snake)
        window.display_text(f'{snake.head_x, snake.head_y}', GameWindow.red, 50,50)
        window.display()
        clock.tick(60)
