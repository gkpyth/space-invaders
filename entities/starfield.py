import pygame
import random
from settings import *

class Starfield:
    def __init__(self):
        self.stars = []
        for _ in range (150):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            speed = random.uniform(0.5, 2.5)
            size = random.randint(1, 3)
            brightness = random.randint(100, 255)
            self.stars.append([x, y, speed, size, brightness])


    def update(self):
        for star in self.stars:
            star[1] += star[2]
            if star[1] > SCREEN_HEIGHT:
                star[1] = 0
                star[0] = random.randint(0, SCREEN_WIDTH)


    def draw(self, screen):
        for star in self.stars:
            color = (star[4], star[4], star[4])
            pygame.draw.circle(screen, color, (int(star[0]), int(star[1])), star[3])