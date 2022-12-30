import time
import sys
import pygame
from ship import Ship
from laser import Laser
from meteor import Meteor
from score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1280, 720))
        self.win_w, self.win_h = self.window.get_size()
        pygame.display.set_caption('Space shooter')

        self.background = pygame.image.load(
            './graphics/background.png').convert()
        self.bg_music = pygame.mixer.Sound('./sounds/music.wav')
        self.bg_music.set_volume(0.2)
        self.bg_music.play(-1)

        self.scoreboard = Score((self.win_w/2, self.win_h - 20))

        self.meteorites_g = pygame.sprite.Group()
        self.spaceship_g = pygame.sprite.GroupSingle()
        self.laser_g = pygame.sprite.Group()
        self.ship = Ship((self.win_w/2, self.win_h/2),
                         self.spaceship_g, [self.meteorites_g, self.laser_g])

        self.meteor_timer = pygame.event.custom_type()
        pygame.time.set_timer(self.meteor_timer, 400)

        self.clock = pygame.time.Clock()
        self.prev_time = time.time()

    def get_deltatime(self):
        self.dt = time.time() - self.prev_time
        self.prev_time = time.time()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == self.meteor_timer:
                Meteor(self.meteorites_g)

    def update(self):
        self.spaceship_g.update(self.dt)
        self.laser_g.update(self.dt)
        self.meteorites_g.update(self.dt)

    def render(self):
        self.window.blit(self.background, (0, 0))
        self.spaceship_g.draw(self.window)
        self.meteorites_g.draw(self.window)
        self.laser_g.draw(self.window)
        self.scoreboard.display(self.window)

    def run(self):
        while True:
            self.handle_events()
            self.get_deltatime()

            self.update()
            self.render()

            self.clock.tick()
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
