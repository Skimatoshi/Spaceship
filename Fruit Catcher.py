import pygame
from random import randint

pygame.init()
from os.path import join


class Blueberry(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('Fruit_Pixel_Art/Png', 'Berry.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 600

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt


class Watermelon(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('Fruit_Pixel_Art/Png', 'Watermelon.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH /2 , WINDOW_HEIGHT /2 ))
        self.direction = pygame.math.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.bottomleft += self.direction * self.speed * dt


class Background(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))



WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Fruit Catcher')

#######################################################

all_sprites = pygame.sprite.Group()
background_surface = pygame.image.load(join('Fruit_Pixel_Art/Png', 'Banana.png')).convert_alpha()


for i in range(20):
    Background(all_sprites, background_surface)

blueberry = Blueberry(all_sprites)
watermelon = Watermelon(all_sprites)
running = True


while running:
    dt = clock.tick() / 1000

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)

    # drawing
    display_surface.fill('white')
    all_sprites.draw(display_surface)
    pygame.draw.rect(display_surface, 'red', blueberry.rect, 2)
    pygame.draw.rect(display_surface, 'blue', watermelon.rect, 2)
    pygame.draw.line(display_surface, 'black', (WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT))
    pygame.draw.line(display_surface, 'black',  (0, WINDOW_HEIGHT/2), (WINDOW_WIDTH, WINDOW_HEIGHT/2))
    pygame.display.update()

pygame.quit()
