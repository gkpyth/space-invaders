import pygame
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()

    game = Game(screen)

    # game.py should handle all things game logic and rendering - I need the following:
    # a handle_events() method - handles keyboard input, quit events, etc.
    # an update() method - handles moving everything and checking collisions
    # a draw() method - handles rendering everything to the screen
    while True:
        game.handle_events()
        game.update()
        game.draw()
        clock.tick(60)

if __name__ == "__main__":
    main()
