# -*-encoding: utf-8 -*-
#
# @author zdy
#
# December 2018
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, settings, screen):
        # initialize spaceship and its location
        super(Ship, self).__init__()
        self.screen = screen
        self.settings = settings

        # load bmp image and get rectangle
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put spaceship on the bottom of window
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        # buld the spaceship at the specific location
        self.screen.blit(self.image,self.rect)
