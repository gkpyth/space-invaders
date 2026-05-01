# settings.py
# Single source of truth for all project settings


# --- Screen ---
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TITLE = "Space Invaders"


# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)


# --- Player ---
PLAYER_SPEED = 5
PLAYER_BULLET_SPEED = 10
PLAYER_LIVES = 3


# --- Alien ---
ALIEN_ROWS = 4
ALIEN_COLS = 11
ALIEN_SPEED_INITIAL = 1
ALIEN_SPEED_INCREMENT = 0.1
ALIEN_DROP_DISTANCE = 20
ALIEN_SHOOT_INTERVAL = 60
ALIEN_BULLET_SPEED = 5


# --- Shield ---
SHIELD_COUNT = 4


# --- Scoring ---
SCORE_PER_ALIEN = {
    "top": 30,
    "middle": 20,
    "bottom": 10,
}

# --- Assets ---
PLAYER_SPRITE = "assets/images/player_spaceship.png"
ALIEN_SPRITES = {
    "bottom": "assets/images/alien_spaceship_1.png",
    "middle": "assets/images/alien_spaceship_2.png",
    "top": "assets/images/alien_spaceship_3.png",
}
EXPLOSION_SPRITE = "assets/images/explosion.png"

# --- Sounds ---
SOUND_SHOOT = "assets/sounds/shoot.wav"
SOUND_EXPLOSION = "assets/sounds/explosion.wav"
SOUND_PLAYER_HIT = "assets/sounds/player_hit.wav"
SOUND_GAME_OVER = "assets/sounds/game_over.wav"
SOUND_LEVEL_COMPLETE = "assets/sounds/level_complete.wav"
SOUND_MUSIC = "assets/sounds/music.mp3"