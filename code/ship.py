import sys
import pygame
from laser import Laser


class Ship(pygame.sprite.Sprite):
    def __init__(self, pos, groups, external_g):
        super().__init__(groups)
        self.external_g = external_g
        self.image = pygame.image.load('./graphics/ship.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.laser_sound = pygame.mixer.Sound('./sounds/laser.ogg')
        self.laser_sound.set_volume(0.4)

        self.direction = pygame.math.Vector2()
        self.speed = 400
        self.health = 20
        self.can_shoot = True
        self.shoot_time = None

    def set_shoot_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 300:
                self.can_shoot = True

    def shoot(self):
        self.laser_sound.play()
        Laser(self.rect.center, self.external_g[1], self.external_g[0])

    def check_collision(self):
        if pygame.sprite.spritecollide(self, self.external_g[0], True, pygame.sprite.collide_mask):
            print(self.health)
            self.health -= 5
            if self.health <= 0:
                pygame.quit()
                sys.exit()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_s] and self.can_shoot:
            self.shoot()
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def move(self, dt):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.y += round(self.direction.y * self.speed * dt)
        self.rect.x += round(self.direction.x * self.speed * dt)

    def update(self, dt):
        self.set_shoot_timer()
        self.input()
        self.move(dt)
        self.check_collision()
