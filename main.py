import pygame
from os.path import join
from random import randint, uniform


# Classes

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png'))
        self.image = pygame.transform.rotate(self.image, -90).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()
        self.speed = 600

        # cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def laser_timer(self):
        # only able to run if self.can_shoot == False:
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midright, all_sprites)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        self.laser_timer()


class Star(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = surf.get_rect(topleft=pos)
        self.speed = 200
        self.direction = pygame.Vector2(5, 5)

    def update(self, dt):
        self.rect.center += dt * self.speed * self.direction
        if self.rect.x > WINDOW_WIDTH:
            self.rect.x = 0
        if self.rect.y > WINDOW_HEIGHT:
            self.rect.y = 0


class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.image = pygame.transform.rotate(self.image, -90).convert_alpha()
        self.rect = self.image.get_frect(midbottom=pos)
        self.direction = pygame.Vector2(1, 0)
        self.speed = 500

    def update(self, dt):
        self.rect.center += self.speed * self.direction * dt

        if self.rect.left > WINDOW_WIDTH:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 2000
        self.speed = 200
        self.direction = pygame.Vector2(uniform(-0.50, -0.5), 1)

    def update(self, dt):
        self.rect.center += self.speed * self.direction * dt
        if self.rect.bottom < 0:
            self.kill()


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

# laser
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()

# meteor
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# Sprites

all_sprites = pygame.sprite.Group()
star_pos = [pygame.Vector2(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(40)]
for pos in star_pos:
    print(pos)
    star = Star(star_surf, pos, all_sprites)
player = Player(all_sprites)


# Custom events -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)



running = True

while running:

    dt = clock.tick() / 1000

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == meteor_event:
            x, y = randint(1180, 1280), randint(-50,-10)
            Meteor(meteor_surf, (x, y), all_sprites)


    all_sprites.update(dt)

    # drawing the game
    screen.fill('gray14')


    all_sprites.draw(screen)

    clock.tick()
    pygame.display.update()
pygame.quit()
