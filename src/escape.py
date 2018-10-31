#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:32:36 2018

@author: crantu
"""

from gpiozero import LED
from time import time


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
