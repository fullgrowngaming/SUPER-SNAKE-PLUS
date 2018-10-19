import pygame, time, sys, random
pygame.init()
from GameWindow import GameWindow
from Snake import Snake
from Collectible import Collectible

if __name__ == "__main__":
    window = GameWindow(800, 600)
    snake = Snake()
    collectibles = []
    clock = pygame.time.Clock()
    running = True

    while running:
        window.window.fill(GameWindow.white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #generate new collectibles
        if not collectibles:
            collectibles.append(Collectible())
        if random.randint(0,120) == 1: #should generate 1 new collectible every 2 seconds???
            collectibles.append(Collectible())

        #handles keypresses and moving the snake
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and snake.direction != 'east':
            snake.direction = 'west'
        elif pressed[pygame.K_RIGHT] and snake.direction != 'west':
            snake.direction = 'east'
        elif pressed[pygame.K_UP] and snake.direction != 'south':
            snake.direction = 'north'
        elif pressed[pygame.K_DOWN] and snake.direction != 'north':
            snake.direction = 'south'

        #move snake and handle screen boundaries (wrap-around)
        snake.move()
        if snake.head_x <= 0 - snake.width:
            snake.head_x = window.res_x
        if snake.head_x > window.res_x:
            snake.head_x = 0
        if snake.head_y <= 0 - snake.height:
            snake.head_y = window.res_y
        if snake.head_y > window.res_y:
            snake.head_y = 0

        #handles collectibles
        for collectible in collectibles:
            collectible.exist_timer += 1
            if collectible.exist_timer >= 300:
                collectibles.remove(collectible)
            if (snake.head_x < collectible.loc_x < snake.head_x + snake.width) and (snake.head_y < collectible.loc_y < snake.head_y + snake.height):
                collectibles.remove(collectible)
                snake.score += 1

        #draws objects and text
        window.draw_snake(snake)
        for collectible in collectibles:
            window.draw_collectible(collectible)
        window.display_text(f'{snake.score}', GameWindow.red, 50,50)

        #update screen and tick
        window.display()
        clock.tick(60)
