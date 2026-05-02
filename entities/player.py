import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        raw = pygame.image.load(PLAYER_SPRITE).convert_alpha()
        self.image = pygame.transform.scale(raw, (60, 60))

        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20

        self.speed = PLAYER_SPEED
        self.lives = PLAYER_LIVES
        self.can_shoot = True
        self.shoot_cooldown = 0

        self.hit_flash = False
        self.flash_timer = 0
        self.flash_duration = 40    # 40 frames


    def update(self):
        self._move()
        self._handle_cooldown()
        self._handle_flash()


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
            self.can_shoot = False
            self.shoot_cooldown = 20
            return True
        return False


    def _handle_flash(self):
        if self.hit_flash:
            self.flash_timer += 1
            # Alternate visibility every 5 frames for the flicker effect
            if self.flash_timer % 5 == 0:
                if self.image.get_alpha() == 255:
                    self.image.set_alpha(50)
                else:
                    self.image.set_alpha(255)
            if self.flash_timer >= self.flash_duration:
                self.hit_flash = False
                self.flash_timer = 0
                self.image.set_alpha(255)


    def take_hit(self):
        self.lives -= 1
        self.hit_flash = True
        self.flash_timer = 0
