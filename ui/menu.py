import pygame
import math
from settings import *

class MenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.SysFont("monospace", 72, bold=True)
        self.font_sub = pygame.font.SysFont("monospace", 28)
        self.font_small = pygame.font.SysFont("monospace", 20)
        self.pulse_timer = 0


    def update(self):
        self.pulse_timer += 0.05


    def draw(self):
        self._draw_title()
        self._draw_subtitle()
        self._draw_controls()


    def _draw_title(self):
        title = "SPACE INVADERS"

        # Shadow layers
        shadow_colors = [
            (0, 20, 80),
            (0, 40, 120),
            (0, 80, 180),
            (0, 120, 220),
            (0, 180, 255),
        ]

        for i, color in enumerate(shadow_colors):
            offset = len(shadow_colors) - i
            surface = self.font_title.render(title, True, color)
            rect = surface.get_rect(center=(SCREEN_WIDTH // 2 + offset, SCREEN_HEIGHT // 3 + offset))
            self.screen.blit(surface, rect)

        # Top layer brightest white-blue
        top = self.font_title.render(title, True, (200, 230, 255))
        rect = top.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(top, rect)


    def _draw_subtitle(self):
        # Use sine wave method to pulse alpha
        alpha = int((math.sin(self.pulse_timer) + 1) / 2 * 200 + 55)

        text = self.font_sub.render("PRESS ENTER TO PLAY", True, YELLOW)
        text.set_alpha(alpha)
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
        self.screen.blit(text, rect)


    def _draw_controls(self):
        controls = [
            "LEFT / RIGHT ARROW — Move",
            "SPACE — SHOOT",
            "R — Restart  |  ESC — Quit"
        ]
        for i, line in enumerate(controls):
            text = self.font_small.render(line, True, (150, 150, 150))
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130 + i * 30))
            self.screen.blit(text, rect)