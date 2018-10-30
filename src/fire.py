#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:34:15 2018

@author: crantu
"""

from gpiozero import LED
from time import time


class Fire:
    def __init__(self, led_fire_pin):
        self.led_fire = LED(led_fire_pin)

    def on(self):
        start_time = time()
        self.led_fire.on()
        print("fire on")
        return time() - start_time

    def off(self):
        start_time = time()
        self.led_fire.off()
        print("fire off")
        return time() - start_time
