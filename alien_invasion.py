# -*-encoding: utf-8 -*-
#
# @author zdy
#
# December 2018
import pygame

import game_functions as gf
from contants import settings
from ship import Ship


def run_game():
    # initialize game and create a dispaly object
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(settings, screen)
    pygame.display.set_caption("Alien Invasion")

    # game loop
    while True:
        # supervise keyboard and mouse item
        gf.check_events(ship)
        gf.update_screen(settings, screen, ship)
        ship.update()


if __name__ == '__main__':
    run_game()
