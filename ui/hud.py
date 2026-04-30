import pygame
from settings import *

class HUD:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.SysFont("monospace", 36, bold=True)
        self.font_small = pygame.font.SysFont("monospace", 24)


    def draw(self, score, lives, state):
        self._draw_score(score)
        self._draw_lives(lives)
        if state == "game_over":
            self._draw_game_over()
        if state == "win":
            self._draw_win()


    def _draw_score(self, score):
        text = self.font_small.render(f"Score: {score}", True, WHITE)
        self.screen.blit(text, (20, 15))


    def _draw_lives(self, lives):
        text = self.font_small.render(f"Lives: {lives}", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH - 150, 15))


    def _draw_game_over(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        text = self.font_large.render("GAME OVER", True, RED)
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        self.screen.blit(text, rect)

        sub = self.font_small.render("Press R to restart", True, WHITE)
        sub_rect = sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        self.screen.blit(sub, sub_rect)


    def _draw_win(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        text = self.font_large.render("YOU WIN!", True, GREEN)
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        self.screen.blit(text, rect)

        sub = self.font_small.render("Press R to restart", True, WHITE)
        sub_rect = sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        self.screen.blit(sub, sub_rect)
