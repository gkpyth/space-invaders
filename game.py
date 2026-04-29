import pygame
from settings import *

from entities.player import Player
from entities.bullet import Bullet

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


    def update(self):
        self.all_sprites.update()


    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
