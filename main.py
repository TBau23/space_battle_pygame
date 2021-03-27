import pygame
import os

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game time baby")

WHITE = (255, 255, 255)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 65, 55

FPS = 60

YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

RED_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

BACKGROUND = pygame.image.load(os.path.join('Assets', 'above_earth.png'))


def draw_window(red, yellow):
    WINDOW.fill(WHITE)
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) # order of drawing matters. Spaceship would not be visible if we had done it before color fill
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # controls speed of while loop - run it 60 times per second at maximum
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        yellow.x += 1
        draw_window(red, yellow)
        

    pygame.quit()

if __name__ == "__main__": #only run main if we directly run this file
    main()
