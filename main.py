import pygame
from os.path import join
from random import randint

# Initializing the game
pygame.init()

# General setup
clock = pygame.time.Clock()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Spaceship Game')

# Importing images
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_surf = pygame.transform.rotate(player_surf, -90).convert_alpha()
player_rect = player_surf.get_frect(bottomright= (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_speed = 300
star_pos = [pygame.Vector2(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(30)]
star_direction = pygame.Vector2(5, 5)
running = True

while running:

    dt = clock.tick(60) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player_rect.centerx += 5

    # drawing the game
    screen.fill('gray14')

    for pos in star_pos:
        pos += dt * star_speed * star_direction
        if pos.x > WINDOW_WIDTH:
            pos.x = 0
        if pos.y > WINDOW_HEIGHT:
            pos.y = 0
        screen.blit(star_surf, pos)

    screen.blit(player_surf, player_rect)
    if player_pos.x > WINDOW_WIDTH:
        player_pos.x = 0

    pygame.display.update()
    clock.tick(60)
pygame.quit()
