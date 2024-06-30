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
        global amount_of_shots
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            amount_of_shots += 1
            Laser(laser_surf, self.rect.midright, (all_sprites, laser_sprites))
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
        self.speed = 1000

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
        self.speed = 100
        self.direction = pygame.Vector2(-5, uniform(-0.5, 1))

    def update(self, dt):
        self.rect.center += self.speed * self.direction * dt
        if self.rect.bottom < 0:
            self.kill()


def collisions():
    global running
    player_meteor_collision = pygame.sprite.spritecollide(player, meteor_sprites, True)
    if player_meteor_collision:
        running = False

    for laser in laser_sprites:
        if pygame.sprite.spritecollide(laser, meteor_sprites, True):
            laser.kill()


def display_score():
    current_time = pygame.time.get_ticks() // 100
    text_surf = font.render(str(current_time), True, (250, 250, 250))
    text_rect = text_surf.get_frect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
    score_surf = laser_shot_font.render(f'Shots made: {amount_of_shots}', True, (240, 240, 240))
    score_rect = score_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))
    screen.blit(text_surf, text_rect)
    screen.blit(score_surf, score_rect)
    pygame.draw.rect(screen, (240, 240, 240), text_rect.inflate(20, 16).move(0, -10), 5, 10)


# Initializing the game
pygame.init()

# General setup
amount_of_shots = 0sa
clock = pygame.time.Clock()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Spaceship Game')

# Importing images

player_direction = pygame.math.Vector2(0, 0)
player_speed = 600

# star
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
font = pygame.font.Font(join('images', 'Oxanium-Bold.ttf'), 30)
laser_shot_font = pygame.font.Font(join('images', 'Oxanium-Bold.ttf'), 20)

# Sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

star_pos = [pygame.Vector2(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(40)]
for pos in star_pos:
    Star(star_surf, pos, all_sprites)
player = Player(all_sprites)

# Custom events -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 300)

running = True

test_rect = pygame.FRect(0, 0, 300, 600)

while running:

    dt = clock.tick() / 1000

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == meteor_event:
            x, y = 1280, randint(20, 600)
            Meteor(meteor_surf, (x, y), (all_sprites, meteor_sprites))

    all_sprites.update(dt)
    collisions()

    # drawing the game
    screen.fill('#3a2e3f')

    all_sprites.draw(screen)
    display_score()

    pygame.display.update()
pygame.quit()
