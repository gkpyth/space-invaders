import pygame
from settings import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        raw = pygame.image.load(EXPLOSION_SPRITE).convert_alpha()
        self.image = pygame.transform.scale(raw, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.lifetime = 10      # visible for 20 frames
        self.timer = 0


    def update(self):
        self.timer += 1
        # Fade out by reducing alpha overtime - not suddenly
        alpha = max(0, 255 - (255 * self.timer // self.lifetime))
        self.image.set_alpha(alpha)
        if self.timer >= self.lifetime:
            self.kill()