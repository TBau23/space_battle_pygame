import pygame
import os

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game time baby")

VELOCITY = 5
BULLET_VEL = 7
MAX_BULLETS = 3
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 65, 55
FPS = 60

YELLOW_GOT_HIT = pygame.USEREVENT + 1 # code for custom user events that we can check for and handle
RED_GOT_HIT = pygame.USEREVENT + 2

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
    if keys_pressed[pygame.K_a] and red.x - VELOCITY > 0: # LEFT for red ship
        red.x -= VELOCITY
    if keys_pressed[pygame.K_d] and red.x + VELOCITY + red.width < BORDER.x: # RIGHT
        red.x += VELOCITY
    if keys_pressed[pygame.K_w] and red.y - VELOCITY > 0: #UP
        red.y -= VELOCITY
    if keys_pressed[pygame.K_s] and red.y + VELOCITY + red.height < HEIGHT - 15: #DOWN
        red.y += VELOCITY

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VELOCITY > BORDER.x: # LEFT for yellow ship
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VELOCITY + yellow.width < WIDTH: # RIGHT
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_UP] and yellow.y - VELOCITY > 0: #UP
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and yellow.y + VELOCITY + yellow.height < HEIGHT - 15: #DOWN
        yellow.y += VELOCITY


def draw_window(red, yellow, red_bullets, yellow_bullets):
    WINDOW.fill(WHITE)
    pygame.draw.rect(WINDOW, BLACK, BORDER)
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) # order of drawing matters. Spaceship would not be visible if we had done it before color fill
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, BLACK, bullet)


    pygame.display.update()

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    # loop through red bullets and check if they hit end of screen or collide with other character 
    # vice versa for yellow
    for bullet in red_bullets:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_GOT_HIT))
            red_bullets.remove(bullet)

    for bullet in yellow_bullets:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet): 
            pygame.event.post(pygame.event.Event(RED_GOT_HIT))
            yellow_bullets.remove(bullet)

def main():
    red = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(850, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # controls speed of while loop - run it 60 times per second at maximum
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height // 2 - 2, 10, 5) # display x, display y, rect width, rect height
                    red_bullets.append(bullet)
                
                if event.key == pygame.K_RSHIFT and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x, yellow.y + yellow.height // 2 - 2, 10, 5) # display x, display y, rect width, rect height
                    yellow_bullets.append(bullet)

        
        keys_pressed = pygame.key.get_pressed()
        handle_red_movement(keys_pressed, red)
        handle_yellow_movement(keys_pressed, yellow)

        handle_bullets(yellow_bullets, red_bullets, red, yellow)
        
        draw_window(red, yellow, red_bullets, yellow_bullets)
        

    pygame.quit()

if __name__ == "__main__": #only run main if we directly run this file
    main()
