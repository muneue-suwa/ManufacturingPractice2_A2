#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:36:10 2018

@author: crantu
"""

from gpiozero import LED
from time import time


class Conveyor:
    def __init__(self, motor_conveyor_pin):
        self.motor_conveyor = LED(motor_conveyor_pin)

    def on(self):
        start_time = time()
        self.motor_conveyor.on()
        print("conveyor on")
        return time() - start_time

    def off(self):
        start_time = time()
        self.motor_conveyor.off()
        print("conveyor off")
        return time() - start_time
