import asyncio
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, FPS
from game import Game

async def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    game = Game(screen)

    while True:
        game.handle_events()
        game.update()
        game.draw()
        clock.tick(FPS)
        await asyncio.sleep(0)      # yields control back to browser each frame — without it, doesn't work

asyncio.run(main())
