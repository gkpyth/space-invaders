import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, color, speed=None):
        super().__init__()

        self.image = pygame.Surface((4, 15))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y

        self.direction = direction      # -1 = up (player bullet) | 1 = down (alien bullet)
        if speed is not None:
            self.speed = speed
        else:
            self.speed = PLAYER_BULLET_SPEED if direction == -1 else ALIEN_BULLET_SPEED


    def update(self):
        self.rect.y += self.speed * self.direction
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()