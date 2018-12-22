# -*-encoding: utf-8 -*-
#
# @author zdy
#
# December 2018
import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from contants import settings
from game_stats import GameStats
from score_board import Scoreboard
from ship import Ship


def run_game():
    # initialize game and create a dispaly object
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(screen, "Play")

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()
