#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:32:34 2018

@author: crantu
"""

from siren import Siren
from conveyor import Conveyor
from fire import Fire

from time_calculator import fire_and_conveyor_time

# audiofiles_dir = "../../MP2_A2_audiofiles/"
# siren_mp3 = "ambulance-siren2.mp3"

sorted_items, wating_times = fire_and_conveyor_time()
print(sorted_items)
class FireAndConveyor:
    def __init__(self, led_siren_pin, audiofiles_dir,
                 motor_conveyor_pin,
                 led_fire_pin):

        siren = Siren(led_siren_pin, audiofiles_dir)
        conveyor = Conveyor(motor_conveyor_pin)
        fire = Fire(led_fire_pin)

        sorted_items, wating_times = fire_and_conveyor_time()
        print(sorted_items)








if __name__ == "__main__":
    led_siren_pin_fig = 17
    conveyour_pin_fig = 18

    conveyor = Conveyor(conveyour_pin_fig)
    siren = Siren(led_siren_pin_fig, "../../MP2_A2_audiofiles/")

    conveyor.on()
    siren.on()
    sleep(10)
    siren.off()
    conveyor.off()
