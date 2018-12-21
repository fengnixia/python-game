# -*-encoding: utf-8 -*-
#
# @author zdy
#
# December 2018
import pygame
import sys


def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        # move right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move left
        ship.moving_left = True


def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    # respond to  keyboard and mouse item
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(settings, screen, ship):
    # fill color
    screen.fill(settings.bg_color)
    ship.blitme()
    # visualiaze the window
    pygame.display.flip()
