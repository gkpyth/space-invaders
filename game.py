import pygame
from settings import *

from entities.player import Player
from entities.bullet import Bullet
from entities.shield import create_shield
from entities.starfield import Starfield
from entities.explosion import Explosion

from managers.wave_manager import WaveManager
from managers.sound_manager import SoundManager
from managers.score_manager import ScoreManager

from ui.hud import HUD
from ui.menu import MenuScreen

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = "menu"      # "menu", "playing", "level_complete", "dropping", "warping",  "game_over", "win"
        self.level = 1

        # Menu
        self.menu = MenuScreen(self.screen)

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
        self.shields = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

        # Entities
        self.player = Player()
        self.all_sprites.add(self.player)

        # Managers
        self.wave_manager = WaveManager(self.aliens,self.alien_bullets,self.all_sprites)
        self.sound_manager = SoundManager()
        self.score_manager = ScoreManager()
        self.starfield = Starfield()
        self.hud = HUD(screen)

        # Game state
        self.score = 0
        self.warp_timer = 0
        self.level_complete_timer = 0

        # Shield
        self._spawn_shields()


    def _spawn_shields(self):
        shield_y = SCREEN_HEIGHT - 160
        total_width = 100       # approximate shield width
        spacing = SCREEN_WIDTH // (SHIELD_COUNT + 1)
        for i in range(SHIELD_COUNT):
            x = spacing * (i + 1) - total_width // 2
            create_shield(x, shield_y, self.shields, self.all_sprites)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.state == "menu":
                    self.state = "playing"
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_SPACE and self.state == "playing":
                    if self.player.shoot():
                        self.sound_manager.play("shoot")
                        bullet = Bullet(
                            self.player.rect.centerx,
                            self.player.rect.top,
                            direction = -1,
                            color = YELLOW
                        )
                        self.player_bullets.add(bullet)
                        self.all_sprites.add(bullet)

                if event.key == pygame.K_r and self.state in ("game_over", "win"):
                    self.__init__(self.screen)


    def update(self):
        self.starfield.update()

        if self.state == "menu":
            return

        if self.state == "level_complete":
            self.level_complete_timer += 1
            self.explosions.update()        # keeps fading after last alien killed; without it, last alien's explosion remains on screen throughout the travel animation
            if self.level_complete_timer >= 90:     # 90 frames = ~1.5 seconds
                self._start_warp()
            return

        if self.state == "warping":
            self.warp_timer += 1
            self.explosions.update()        # keeps fading after last alien killed
            # Ship races upward
            self.player.rect.y -= 6
            if self.warp_timer >= WARP_DURATION:
                self._start_next_level()
            return

        if self.state == "dropping":
            self.wave_manager.update()
            if not self.wave_manager.dropping:
                self.state = "playing"
            return

        if self.state != "playing":
            return

        self.all_sprites.update()
        self.wave_manager.update()
        self._check_collisions()


    def _start_warp(self):
        self.state = "warping"
        self.warp_timer = 0
        self.starfield.set_warp(True)
        # Kill all shields and bullets
        for sprite in self.shields.sprites():
            sprite.kill()
        for sprite in self.alien_bullets.sprites():
            sprite.kill()
        for sprite in self.player_bullets.sprites():
            sprite.kill()


    def _start_next_level(self):
        self.starfield.set_warp(False)
        self.level += 1
        # Reset player position
        self.player.rect.centerx = SCREEN_WIDTH // 2
        self.player.rect.bottom = SCREEN_HEIGHT - 20
        # Spawn new wave in drop-in mode
        self.wave_manager.next_level(self.level)
        # Respawn shields
        self._spawn_shields()
        self.state = "dropping"


    def _check_collisions(self):
        # Player bullets hit aliens
        hits = pygame.sprite.groupcollide(
            self.aliens,
            self.player_bullets,
            True,       # True = kill alien on hit
            True        # True = kill bullet on hit
        )
        for alien in hits:
            self.score += alien.points
            self.sound_manager.play("explosion")
            explosion = Explosion(alien.rect.centerx, alien.rect.centery)
            self.all_sprites.add(explosion)
            self.explosions.add(explosion)
            self.wave_manager.on_alien_killed()     # fix for increase speed per alien killed logic - updating speed the moment alien dies

        # Player bullets hit shields
        hits = pygame.sprite.groupcollide(self.shields, self.player_bullets, False, True)
        for block in hits:
            block.hit()

        # Alien bullets hit shields
        hits = pygame.sprite.groupcollide(self.shields, self.alien_bullets, False, True)
        for block in hits:
            block.hit()

        # Aliens destroy shields on contact
        hits = pygame.sprite.groupcollide(self.shields, self.aliens, False, False)
        for block in hits:
            block.hit()

        # Alien bullets hit player
        if pygame.sprite.spritecollide(self.player, self.alien_bullets, True):
            self.sound_manager.play("player_hit")
            self.player.take_hit()
            if self.player.lives <= 0:
                self.sound_manager.play("game_over")
                self.score_manager.save(self.score)
                self.state = "game_over"

        # Aliens reach the player
        for alien in self.aliens:
            if alien.rect.bottom >= self.player.rect.top:
                self.sound_manager.play("game_over")
                self.score_manager.save(self.score)
                self.state = "game_over"

        # All aliens cleared
        if len(self.aliens) == 0:
            self.score_manager.save(self.score)
            for sprite in self.alien_bullets.sprites():
                sprite.kill()
            for sprite in self.player_bullets.sprites():
                sprite.kill()
            if self.level >= TOTAL_LEVELS:
                self.sound_manager.play("level_complete")
                self.state = "win"
            else:
                self.sound_manager.play("level_complete")
                self.level_complete_timer = 0
                self.state = "level_complete"


    def draw(self):
        self.screen.fill(BLACK)
        self.starfield.draw(self.screen)

        if self.state == "menu":
            self.menu.update()
            self.menu.draw()
            pygame.display.flip()
            return

        self.all_sprites.draw(self.screen)
        self.hud.draw(self.score, self.player.lives, self.state, self.score_manager.high_score, self.level)
        pygame.display.flip()






