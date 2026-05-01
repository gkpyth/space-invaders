import pygame
from settings import *

class ShieldBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((10, 10))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y

        self.health = 3


    def hit(self):
        self.health -= 1
        if self.health == 2:
            self.image.fill((0, 180, 0))    # Darker green
        elif self.health == 1:
            self.image.fill((0, 100, 0))    # Even darker green
        else:
            self.kill()


def create_shield(x, y, shields_group, all_sprites_group):
    # Shield shape as a grid pattern (1 = block, 0 = empty)
    shape = [
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
    ]
    block_size = 10

    for row_idx, row in enumerate(shape):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                block = ShieldBlock(
                    x + col_idx * block_size,
                    y + row_idx * block_size
                )
                shields_group.add(block)
                all_sprites_group.add(block)