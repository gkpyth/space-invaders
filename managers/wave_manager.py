import pygame
import random

from settings import *
from entities.alien import Alien
from entities.bullet import Bullet

class WaveManager:
    def __init__(self, aliens_group, alien_bullets_group, all_sprites_group):
        self.aliens = aliens_group
        self.alien_bullets = alien_bullets_group
        self.all_sprites = all_sprites_group

        self.direction = 1          # 1 = right, -1 = left
        self.speed = ALIEN_SPEED_INITIAL
        self.shoot_timer = 0

        self._spawn_wave()


    def _spawn_wave(self):
        # Define spacing between aliens
        x_spacing = 70
        y_spacing = 55
        x_start = 100
        y_start = 80

        for row in range(ALIEN_ROWS):
            for col in range(ALIEN_COLS):
                alien = Alien(row, col)
                alien.rect.x = x_start + col * x_spacing
                alien.rect.y = y_start + row * y_spacing
                self.aliens.add(alien)
                self.all_sprites.add(alien)


    def update(self):
        self._move_aliens()
        self._alien_shoot()


    def _move_aliens(self):
        # Check if any alien hits a wall
        drop = False
        for alien in self.aliens:
            if self.direction == 1 and alien.rect.right >= SCREEN_WIDTH - 20:
                drop = True
                break
            if self.direction == -1 and alien.rect.left <= 20:
                drop = True
                break

        if drop:
            self.direction *= -1
            for alien in self.aliens:
                alien.rect.y += ALIEN_DROP_DISTANCE
        else:
            for alien in self.aliens:
                alien.rect.x += self.speed * self.direction

        # Speed up aliens as they are killed
        aliens_killed = (ALIEN_ROWS * ALIEN_COLS) - len(self.aliens)
        self.speed = ALIEN_SPEED_INITIAL + (aliens_killed * ALIEN_SPEED_INCREMENT)


    def _alien_shoot(self):
        self.shoot_timer += 1
        if self.shoot_timer >= ALIEN_SHOOT_INTERVAL:
            self.shoot_timer = 0
            if self.aliens:
                shooter = random.choice(self.aliens.sprites())
                bullet = Bullet(
                    shooter.rect.centerx,
                    shooter.rect.bottom,
                    direction = 1,
                    color = RED
                )
                self.alien_bullets.add(bullet)
                self.all_sprites.add(bullet)