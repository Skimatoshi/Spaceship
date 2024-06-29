import pygame
from os.path import join
from random import randint


# Classes

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png'))
        self.image = pygame.transform.rotate(self.image, -90).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()
        self.speed = 600

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('fire laser')


class Star(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.star_pos = [pygame.Vector2(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(40)]
        self.speed = 600
        self.direction = pygame.Vector2(5, 5)

    def update(self, dt):
        for pos in self.star_pos:
            pos += dt * self.speed * self.direction
            if pos.x > WINDOW_WIDTH:
                pos.x = 0
            if pos.y > WINDOW_HEIGHT:
                pos.y = 0


# Initializing the game
pygame.init()

# General setup
clock = pygame.time.Clock()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Spaceship Game')

# Importing images

player_direction = pygame.math.Vector2(0, 0)
player_speed = 600

# star
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()

# meteor
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# laser
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

# Sprites

all_sprites = pygame.sprite.Group()

star = Star(star_surf, all_sprites)
player = Player(all_sprites)

running = True

while running:

    dt = clock.tick() / 1000

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)

    # drawing the game
    screen.fill('gray14')

    screen.blit(meteor_surf, meteor_rect)
    screen.blit(laser_surf, laser_rect)

    all_sprites.draw(screen)

    clock.tick()
    pygame.display.update()
pygame.quit()
