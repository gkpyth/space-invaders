import pygame
from settings import *

class SoundManager:
    def __init__(self):
        # Sound Effects
        self.sounds = {
            "shoot": pygame.mixer.Sound(SOUND_SHOOT),
            "explosion": pygame.mixer.Sound(SOUND_EXPLOSION),
            "player_hit": pygame.mixer.Sound(SOUND_PLAYER_HIT),
            "game_over": pygame.mixer.Sound(SOUND_GAME_OVER),
            "level_complete": pygame.mixer.Sound(SOUND_LEVEL_COMPLETE),
        }

        # Background Music
        pygame.mixer.music.load(SOUND_MUSIC)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)     # -1 loops indefinitely

        # Adjust volumes individually
        self.sounds["shoot"].set_volume(0.2)
        self.sounds["explosion"].set_volume(0.1)
        self.sounds["player_hit"].set_volume(0.5)
        self.sounds["game_over"].set_volume(0.8)
        self.sounds["level_complete"].set_volume(0.8)


    def play(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()