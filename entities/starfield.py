import pygame
import random
from settings import *

class Starfield:
    def __init__(self):
        self.stars = []
        self.warp_mode = False
        self.warp_intensity = 0     # 0 to 1, ramps up during warp
        for _ in range (150):
            self._add_star()

    def _add_star(self, y=None):
        x = random.randint(0, SCREEN_WIDTH)
        y = y if y is not None else random.randint(0, SCREEN_HEIGHT)
        speed = random.uniform(0.5, 2.5)
        size = random.randint(1, 3)
        brightness = random.randint(100, 255)
        self.stars.append([x, y, speed, size, brightness])


    def set_warp(self, active):
        self.warp_mode = active
        if not active:
            self.warp_intensity = 0


    def update(self):
        if self.warp_mode:
            self.warp_intensity = min(1.0, self.warp_intensity + 0.02)
            warp_speed = 60 * self.warp_intensity
        else:
            warp_speed = 0

        for star in self.stars:
            star[1] += star[2] + warp_speed
            if star[1] > SCREEN_HEIGHT:
                star[1] = 0
                star[0] = random.randint(0, SCREEN_WIDTH)


    def draw(self, screen):
        for star in self.stars:
            color = (star[4], star[4], star[4])
            if self.warp_mode and self.warp_intensity > 0.1:
                # Draw stretched lines instead of dots
                trail_length = int(40 * self.warp_intensity * star[2])
                start_pos = (int(star[0]), int(star[1]))
                end_pos = (int(star[0]), int(star[1]) - trail_length)
                pygame.draw.line(screen, color, start_pos, end_pos, star[3])
            else:
                pygame.draw.circle(screen, color, (int(star[0]), int(star[1])), star[3])