#Title: Alien Invasion
#File: alien_invasion.py
#Author: Matt Keplinger
#Date: 16 Aug 2021

import sys
import pygame
from settings import Settings
from ship import Ship

class Alien_Invasion:
    #Initialize Alien Invasion and create game resources
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    #Check for mouse and keyboard events
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    #Respond to Key Release
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    #Respond to Key Press
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    #Update images on screen, flip to a new screen
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

if __name__ == '__main__':
    #Make game instance and run game
    ai = Alien_Invasion()
    ai.run_game()


