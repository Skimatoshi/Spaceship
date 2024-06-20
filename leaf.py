import pygame
from os.path import join
from random import randint

# Player

class Leaf(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('leaf_ranger.png')).convert_alpha()
        self.rect = self.image.get_frect(center= (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 600

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt


class Star(pygame.sprite.Sprite):
    def __init__(self,groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center= (randint(0, WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)))





pygame.init()

# Screen
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Leaf Character')

running = True
clock = pygame.time.Clock()


# Sprites
all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join('space shooter/images' , 'star.png')).convert_alpha()
for i in range(20):
    Star(all_sprites, star_surf)
leaf = Leaf(all_sprites)


while running:

    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # update
    all_sprites.update(dt)

    display_screen.fill('black')

    pygame.draw.rect(display_screen, 'white', leaf.rect, 3)
    pygame.draw.line(display_screen, 'white', (WINDOW_WIDTH/ 2, 0) , (WINDOW_WIDTH / 2, WINDOW_HEIGHT))
    pygame.draw.line(display_screen, 'white', (0, WINDOW_HEIGHT/2) , (WINDOW_WIDTH, WINDOW_HEIGHT / 2))
    all_sprites.draw(display_screen)
    pygame.display.update()

pygame.quit()