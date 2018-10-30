#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:35:37 2018

@author: crantu
"""

from pygame import mixer
from gpiozero import LED
from time import time
from os import path


class Siren:
    def __init__(self, led_siren_pin, audiofiles_dir):
        self.led_siren = LED(led_siren_pin)
        self.mixer_siren = mixer
        self.audiofiles_dir = audiofiles_dir

    def on(self):
        start_time = time()
        siren_mp3_path = path.join(self.audiofiles_dir,
                                   "ambulance-siren2.mp3")
        self.mixer_siren.init()
        self.mixer_siren.music.load(siren_mp3_path)  # 12sec
        self.mixer_siren.music.play(-1)
        self.led_siren.blink()
        print("siren on")
        return time() - start_time

    def off(self):
        start_time = time()
        self.mixer_siren.music.stop()
        self.led_siren.off()
        print("siren off")
        return time() - start_time
