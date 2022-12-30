import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, groups, external_g):
        super().__init__(groups)
        self.external_g = external_g
        self.image = pygame.image.load('./graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 480

    def meteor_collision(self):
        sprites = pygame.sprite.spritecollide(
            self, self.external_g, False, pygame.sprite.collide_mask)
        for sprite in sprites:
            sprite.health -= 5
            self.kill()

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.bottom < 0:
            self.kill()
        self.meteor_collision()
