#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:48:40 2018

@author: crantu
"""

from pygame import mixer
from gpiozero import LED, Button
from time import sleep
from os import path

led_number = 17
button_number = 3


class ExplodeAndEscape:
    def __init__(self,
                 audiofiles_dir,
                 conveyor_time,
                 explosion_wating_time,
                 destroy_crane_time,
                 remove_stopper_time):
        siren_mp3 = "bomb1.mp3 "
        self.bomb_mp3_path = path.join(audiofiles_dir, siren_mp3)
        self.led_siren = LED(led_number)
        self.button = Button(button_number)

    def explode_and_escape():
        pass
