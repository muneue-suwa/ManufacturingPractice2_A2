#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:48:40 2018

@author: crantu
"""

from pygame import mixer
from gpiozero import LED
from time import time
from os import path


class Explode:
    def __init__(self, led_explode_pin, audiofiles_dir):
        self.led_explode = LED(led_explode_pin)
        self.mixer_explode = mixer
        self.audiofiles_dir = audiofiles_dir

    def on(self):
        start_time = time()
        siren_mp3_path = path.join(self.audiofiles_dir, "bomb1.mp3")
        self.mixer_explode.init()
        self.mixer_explode.music.load(siren_mp3_path)
        self.mixer_explode.music.play(1)
        self.led_explode.blink()
        print("siren on")
        return time() - start_time

    def off(self):
        start_time = time()
        self.mixer_explode.music.stop()
        self.led_explode.off()
        print("siren off")
        return time() - start_time


class Escape:
    def __init__(self, motor_escape_pin):
        self.motor_escape = LED(motor_escape_pin)

    def on(self):
        start_time = time()
        self.motor_escape.on()
        print("escape on")
        return time() - start_time

    def off(self):
        start_time = time()
        self.motor_escape.off()
        print("escape off")
        return time() - start_time
