import pygame

# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

acceleration = 0.02
velocity = -2
ball_y = WINDOW_HEIGHT / 2
clock = pygame.time.Clock()

running = True
pygame.display.set_caption('Badminton')
FPS = 60


def add_velocity():
    global velocity
    velocity = -2


def gravity():
    global velocity
    global acceleration
    global ball_y

    ball_y += velocity
    pygame.draw.rect(display_surface, 'black', (WINDOW_HEIGHT, ball_y, 20, 20))
    print(velocity)
    velocity += acceleration


while running:
    clock.tick(FPS)
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                add_velocity()

        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('white')

    gravity()

    pygame.display.update()

pygame.quit()
