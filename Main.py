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

        #handles keypresses and moves the snake
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and snake.direction != 'east':
            snake.direction = 'west'
        elif pressed[pygame.K_RIGHT] and snake.direction != 'west':
            snake.direction = 'east'
        elif pressed[pygame.K_UP] and snake.direction != 'south':
            snake.direction = 'north'
        elif pressed[pygame.K_DOWN] and snake.direction != 'north':
            snake.direction = 'south'
        snake.move()


        #handle screen boundaries (wrap-around)
        if snake.head[0] <= 0 - snake.width:
            snake.head[0] = window.res_x
        if snake.head[0] > window.res_x:
            snake.head[0] = 0
        if snake.head[1] <= 0 - snake.height:
            snake.head[1] = window.res_y
        if snake.head[1] > window.res_y:
            snake.head[1] = 0

        #handles collectibles
        for collectible in collectibles:
            collectible.exist_timer += 1
            if collectible.exist_timer >= 600:
                collectibles.remove(collectible)
            if (snake.head[0] < collectible.loc_x < snake.head[0] + snake.width) and (snake.head[1] < collectible.loc_y < snake.head[1] + snake.height):
                snake.lengthen() #[collectible.loc_x, collectible.loc_y]
                collectibles.remove(collectible)
                snake.score += 1

        #draws objects and text
        window.draw_snake(snake)
        for collectible in collectibles:
            window.draw_collectible(collectible)
        window.display_text(f'{snake.score}', GameWindow.red, 50,50)

        #update screen and tick
        snake.update_segments()
        window.display()
        clock.tick(60)
