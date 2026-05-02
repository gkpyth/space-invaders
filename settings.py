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


# --- Aliens ---
ALIEN_ROWS = 4
ALIEN_COLS = 11
ALIEN_SPEED_INCREMENT = 0.1
ALIEN_DROP_DISTANCE = 20
ALIEN_X_START = 100
ALIEN_X_SPACING = 70
ALIEN_Y_START = 80
ALIEN_Y_SPACING = 55


# --- Shield ---
SHIELD_COUNT = 4


# --- Scoring ---
SCORE_PER_ALIEN = {
    "top": 30,
    "middle": 20,
    "bottom": 10,
}
SCORE_FILE = "data/highscore.json"

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

# --- Levels ---
LEVELS = {
    1: {"alien_speed": 1,   "shoot_interval": 60, "alien_bullet_speed": 5},
    2: {"alien_speed": 1.5, "shoot_interval": 45, "alien_bullet_speed": 6},
    3: {"alien_speed": 2,   "shoot_interval": 30, "alien_bullet_speed": 7},
}
TOTAL_LEVELS = 3
WARP_DURATION = 120
