import pygame
import os

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game time baby")

VELOCITY = 5
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



def is_on_screen(ship):
    if ship.x in range(0, WIDTH) and ship.y in range(0, HEIGHT):
        return True
    return False

def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a]: # LEFT for red ship
        red.x -= VELOCITY
    if keys_pressed[pygame.K_d]: # RIGHT
        red.x += VELOCITY
    if keys_pressed[pygame.K_w]: #UP
        red.y -= VELOCITY
    if keys_pressed[pygame.K_s]: #DOWN
        red.y += VELOCITY

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT]: # LEFT for yellow ship
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT]: # RIGHT
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_UP]: #UP
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN]: #DOWN
        yellow.y += VELOCITY


def draw_window(red, yellow):
    WINDOW.fill(WHITE)
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) # order of drawing matters. Spaceship would not be visible if we had done it before color fill
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(850, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # controls speed of while loop - run it 60 times per second at maximum
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        keys_pressed = pygame.key.get_pressed()
        handle_red_movement(keys_pressed, red)
        handle_yellow_movement(keys_pressed, yellow)
        
        draw_window(red, yellow)
        

    pygame.quit()

if __name__ == "__main__": #only run main if we directly run this file
    main()
