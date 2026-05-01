import pygame
from settings import *

from entities.player import Player
from entities.bullet import Bullet
from entities.shield import create_shield

from managers.wave_manager import WaveManager

from ui.hud import HUD

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.state = "playing"      # "menu", "playing", "game_over", "win"

        # TODO: Replace placeholders with actual groups as I build them.
        # Placeholders for now:
        self.all_sprites = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
        self.shields = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.wave_manager = WaveManager(
            self.aliens,
            self.alien_bullets,
            self.all_sprites
        )

        self._spawn_shields()

        self.score = 0

        self.hud = HUD(screen)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.shoot():
                        bullet = Bullet(
                            self.player.rect.centerx,
                            self.player.rect.top,
                            direction = -1,
                            color = YELLOW
                        )
                        self.player_bullets.add(bullet)
                        self.all_sprites.add(bullet)

                if event.key == pygame.K_r and self.state != "playing":
                    self.__init__(self.screen)


    def update(self):
        self.all_sprites.update()
        self.wave_manager.update()
        self._check_collisions()


    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.hud.draw(self.score, self.player.lives, self.state)
        pygame.display.flip()


    def _check_collisions(self):
        # Player bullets hit aliens
        hits = pygame.sprite.groupcollide(
            self.aliens,
            self.player_bullets,
            True,       # True = kill alien on hit
            True        # True = kill bullet on hit
        )
        for alien in hits:
            self.score += alien.points

        # Alien bullets hit player
        if pygame.sprite.spritecollide(self.player, self.alien_bullets, True):
            self.player.lives -= 1
            if self.player.lives <= 0:
                self.state = "game_over"

        # Aliens reach the player
        for alien in self.aliens:
            if alien.rect.bottom >= self.player.rect.top:
                self.state = "game_over"

        # Player bullets hit shields
        pygame.sprite.groupcollide(self.shields, self.player_bullets, False, True, pygame.sprite.collide_rect)

        # Alien bullets hit shields
        hits = pygame.sprite.groupcollide(self.shields, self.alien_bullets, False, True)
        for block in hits:
            block.hit()

        # Player bullets damage shields too
        hits = pygame.sprite.groupcollide(self.shields, self.player_bullets, False, True)
        for block in hits:
            block.hit()

        # Game won condition
        if len(self.aliens) == 0:
            self.state = "win"


    def _spawn_shields(self):
        shield_y = SCREEN_HEIGHT - 160
        total_width = 100       # approximate shield width
        spacing = SCREEN_WIDTH // (SHIELD_COUNT + 1)
        for i in range(SHIELD_COUNT):
            x = spacing * (i + 1) - total_width // 2
            create_shield(x, shield_y, self.shields, self.all_sprites)
