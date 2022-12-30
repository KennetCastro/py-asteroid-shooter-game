import pygame


class Score:
    def __init__(self, pos):
        self.font = pygame.font.Font('./graphics/subatomic.ttf', 46)
        self.pos = pos

    def display(self, win):
        text = f'Score: {pygame.time.get_ticks()//1000}'
        font_surf = self.font.render(text, True, (200, 200, 200))
        font_rect = font_surf.get_rect(center=self.pos)
        win.blit(font_surf, font_rect)
