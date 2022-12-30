import random
import pygame


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/meteor.png').convert_alpha()
        size = pygame.math.Vector2(
            self.image.get_size()) * random.uniform(0.5, 1.5)

        self.scaled_image = pygame.transform.scale(self.image, size)
        self.image = self.scaled_image
        self.rect = self.image.get_rect(
            center=(random.randint(-20, 1100), random.randint(-100, -10)))
        self.mask = pygame.mask.from_surface(self.image)

        self.explosion_sound = pygame.mixer.Sound('./sounds/explosion.wav')
        self.explosion_sound.set_volume(0.4)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(random.uniform(-0.5, 0.5), 1)
        self.speed = random.randint(400, 600)
        self.health = 10

        self.rotation = 0
        self.rotation_speed = random.randint(20, 50)

    def rotate(self, dt):
        self.rotation += self.rotation_speed * dt
        rotate_surf = pygame.transform.rotozoom(
            self.scaled_image, self.rotation, 1)
        self.image = rotate_surf
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))
        self.rotate(dt)
        if self.rect.top > 720:
            self.kill()
        if self.health <= 0:
            self.explosion_sound.play()
            self.kill()
