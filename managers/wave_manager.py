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
        self.shoot_timer = 0
        self.dropping = False
        self.drop_cooldown = 0

        self._apply_level_config(1)
        self._spawn_wave(drop_in=False)

    def _apply_level_config(self, level):
        config = LEVELS[level]
        self.base_speed = config["alien_speed"]
        self.speed = self.base_speed
        self.shoot_interval = config["shoot_interval"]
        self.alien_bullet_speed = config["alien_bullet_speed"]
        self.drop_cooldown = 0


    def next_level(self, level):
        for alien in self.aliens.sprites():
            alien.kill()
        self.alien_bullets.empty()
        self.direction = 1
        self.shoot_timer = 0
        self._apply_level_config(level)
        self._spawn_wave(drop_in=True)


    def _spawn_wave(self, drop_in=False):
        # Define spacing between aliens
        x_spacing = ALIEN_X_SPACING
        y_spacing = ALIEN_Y_SPACING
        x_start = ALIEN_X_START
        y_start = ALIEN_Y_START

        self.dropping = drop_in
        self.grid_x = float(x_start)        # Track float position for whole grid

        for row in range(ALIEN_ROWS):
            for col in range(ALIEN_COLS):
                alien = Alien(row, col)
                alien.rect.x = x_start + col * x_spacing
                if drop_in:
                    alien.rect.y = -(ALIEN_ROWS - row) * y_spacing
                else:
                    alien.rect.y = y_start + row * y_spacing
                alien.target_y = y_start + row * y_spacing
                self.aliens.add(alien)
                self.all_sprites.add(alien)


    def update(self):
        if self.dropping:
            self._handle_drop_in()
        else:
            self._move_aliens()
            self._alien_shoot()


    def _handle_drop_in(self):
        all_landed = True
        for alien in self.aliens:
            if alien.rect.y < alien.target_y:
                alien.rect.y += 8
                if alien.rect.y >= alien.target_y:
                    alien.rect.y = alien.target_y
                all_landed = False

        if all_landed:
            self.dropping = False


    def _move_aliens(self):
        if self.drop_cooldown > 0:
            self.drop_cooldown -= 1

        # Check if any alien hits a wall
        drop = False
        if self.drop_cooldown == 0:
            for alien in self.aliens:
                if self.direction == 1 and alien.rect.right >= SCREEN_WIDTH - 20:
                    drop = True
                    break
                if self.direction == -1 and alien.rect.left <= 20:
                    drop = True
                    break

        if drop:
            self.direction *= -1
            self.drop_cooldown = 20     # ignore wall checks for 20 frames after dropping (prevents double trigger edge-case)
            for alien in self.aliens:
                alien.rect.y += ALIEN_DROP_DISTANCE
        else:
            # Move float position and apply to rects
            self.grid_x += self.speed * self.direction
            offset = int(self.grid_x)
            for alien in self.aliens:
                alien.rect.x = ALIEN_X_START + alien.col * ALIEN_Y_SPACING + offset


    def on_alien_killed(self):
        aliens_killed = (ALIEN_ROWS * ALIEN_COLS) - len(self.aliens)
        self.speed = self.base_speed + (aliens_killed * ALIEN_SPEED_INCREMENT)


    def _alien_shoot(self):
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_interval:
            self.shoot_timer = 0
            if self.aliens:
                shooter = random.choice(self.aliens.sprites())
                bullet = Bullet(
                    shooter.rect.centerx,
                    shooter.rect.bottom,
                    direction = 1,
                    color = RED,
                    speed=self.alien_bullet_speed
                )
                self.alien_bullets.add(bullet)
                self.all_sprites.add(bullet)