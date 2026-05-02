import pygame
from settings import *

class Alien(pygame.sprite.Sprite):
    def __init__(self, row, col):
        super().__init__()

        self.row = row
        self.col = col
        self.alien_type = self._get_type()
        self.points = SCORE_PER_ALIEN[self.alien_type]

        raw = pygame.image.load(ALIEN_SPRITES[self.alien_type]).convert_alpha()
        self.image = pygame.transform.scale(raw, (58, 48))

        self.rect = self.image.get_rect()


    def _get_type(self):
        if self.row == 0:
            return "top"
        elif self.row in (1, 2):
            return "middle"
        else:
            return "bottom"

    # Movement handled by WaveManager — individual aliens do not move themselves
    def update(self):
        pass
