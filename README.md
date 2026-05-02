# Space Invaders

A personal take on the classic arcade shoot 'em up (Space Invaders) built with Python and Pygame. Defend Earth across 3 escalating waves, destroy alien invaders, protect your shields, and chase the high score. - part of personal bootcamp portfolio projects.

## Features
- Smooth 60 FPS gameplay with Pygame
- 3 levels with increasing alien speed, fire rate, and bullet speed
- Alien grid movement with wall detection and progressive speed scaling
- Destructible shields with per-block health and visual damage states
- Warp transition between levels — starfield stretches into light-speed streaks
- Alien drop-in animation at the start of each wave
- Explosion effects with fade-out on alien death
- Player hit flash effect on taking damage
- Scrolling parallax starfield background
- Persistent high score tracking saved to JSON
- Sound effects and looping background music
- Menu screen with 3D layered title and pulsing subtitle
- Game Over and Win screens with high score detection

## Requirements
- Python 3
- Pygame 2.x

## Installation
```
pip install -r requirements.txt
```

## Sound & Music Files
Sound effect files are included in the repository. Background music is **not included** due to licensing restrictions. To enable music, add your own `.mp3` or `.ogg` file to `assets/sounds/` named:

- `music.mp3` — Looping background track

Free music can be sourced from [OpenGameArt](https://opengameart.org) and [Freesound](https://freesound.org).

If you don't have a music file, comment out the music lines in `managers/sound_manager.py` to run the game without it.

## How to Run
```
python main.py
```

## How to Play
- Use **Left / Right arrow keys** to move your ship
- Press **Space** to shoot
- Destroy all aliens to advance to the next level
- Use shields for cover — they absorb damage but degrade over time
- Don't let aliens reach your ship or you lose
- Clear all 3 waves to win
- Press **R** to restart after Game Over or Win
- Press **Esc** to quit

## Project Structure
```
space_invaders/
├── main.py                  # Entry point and game loop
├── settings.py              # All constants, colors, assets, and level configs
├── game.py                  # Game state manager and main logic
├── entities/
│   ├── player.py            # Player ship — movement, shooting, hit flash
│   ├── alien.py             # Alien sprite — type, points, sprite loading
│   ├── bullet.py            # Bullet sprite — player and alien fire
│   ├── shield.py            # Destructible shield blocks
│   ├── explosion.py         # Explosion fade-out effect
│   └── starfield.py         # Scrolling starfield with warp mode
├── managers/
│   ├── wave_manager.py      # Alien grid movement, shooting, drop-in, level config
│   ├── sound_manager.py     # Sound effects and background music
│   └── score_manager.py     # High score load and save
├── ui/
│   ├── hud.py               # In-game HUD and overlay screens
│   └── menu.py              # Main menu screen
├── assets/
│   ├── images/              # Sprite PNGs (player, aliens, explosion)
│   └── sounds/              # Sound effects and music
└── data/
    └── highscore.json       # Persisted high score (auto-generated)
```

## Scoring
| Alien Type | Points |
|------------|--------|
| Top row    | 30     |
| Middle rows| 20     |
| Bottom rows| 10     |

## Limitations
- Desktop only (no web or mobile version)
- Keyboard controls only
- High score is local (no online leaderboard)
- Background music not included (must be sourced separately)

## Author
Ghaleb Khadra