import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # TODO: Replace placeholder with actual player sprite
        # Placeholder visual for now - simple rectangle
        self.image = pygame.Surface((50,30))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20

        self.speed = PLAYER_SPEED
        self.lives = PLAYER_LIVES
        self.can_shoot = True
        self.shoot_cooldown = 0


    def update(self):
        self._move()
        self._handle_cooldown()


    def _move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 10:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH - 10:
            self.rect.x += self.speed


    def _handle_cooldown(self):
        if not self.can_shoot:
            self.shoot_cooldown -= 1
            if self.shoot_cooldown <= 0:
                self.can_shoot = True


    def shoot(self):
        if self.can_shoot:
            self.can_shoot=False
            self.shoot_cooldown = 20
            return True
        return False