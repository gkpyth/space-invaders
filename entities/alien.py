import pygame
from settings import *

class Alien(pygame.sprite.Sprite):
    def __init__(self, row, col):
        super().__init__()

        self.row = row
        self.col = col
        self.alien_type = self._get_type()
        self.points = SCORE_PER_ALIEN[self.alien_type]

        # TODO: Replace with actual alien sprite
        # Placeholder visual for now - color coded by row
        self.image = pygame.Surface((40,30))
        self.image.fill(self._get_color())

        self.rect = self.image.get_rect()


    def _get_type(self):
        if self.row == 0:
            return "top"
        elif self.row in (1,2):
            return "middle"
        else:
            return "bottom"


    def _get_color(self):
        colors = {
            "top": CYAN,
            "middle": GREEN,
            "bottom": WHITE
        }
        return colors[self.alien_type]


    # TODO: Implement Alien movement in wave_manager.py
    # Wave_manager will handle Alien movement, not individual aliens.
    def update(self):
        pass
