import pygame
from settings import *

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


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


    def update(self):
        self.all_sprites.update()


    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
