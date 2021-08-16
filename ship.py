#Title: Alien Invasion
#File: ship.py
#Author: Matt Keplinger
#Date: 16 Aug 2021

import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

    #Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

    #Start each ship at midbottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

    #Store horizontal position of ship
        self.x = float(self.rect.x)

    #Movement Flag
        self.moving_right = False
        self.moving_left = False

    #Update ship position based on movement flag
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

    #Update rect object from self.x
        self.rect.x = self.x

    #Draw ship at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)

