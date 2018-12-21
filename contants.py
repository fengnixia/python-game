# -*-encoding: utf-8 -*-
#
# @author zdy
#
# December 2018


class Settings(object):
    """docstring for Settings"""
    def __init__(self):
        # initialize setting of game

        # screen setting
        self.screen_width = 750
        self.screen_height = 500
        self.bg_color = (255,255,255)
        self.ship_speed_factor = 1.5


settings = Settings()
