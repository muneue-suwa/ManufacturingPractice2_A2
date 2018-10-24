#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:32:34 2018

@author: crantu
"""

from pygame import mixer
from gpiozero import LED, Button
from time import sleep
from os import path

# audiofiles_dir = "../../MP2_A2_audiofiles/"
# siren_mp3 = "ambulance-siren2.mp3"

led_number = 17
button_number = 3


class FireAndConveyor:
    def __init__(self,
                 audiofiles_dir,
                 conveyor_time,
                 destruction_wating_time,
                 destroy_crane_time,
                 remove_stopper_time):
        siren_mp3 = "ambulance-siren2.mp3"
        self.siren_mp3_path = path.join(audiofiles_dir, siren_mp3)
        self.led_siren = LED(led_number)
        self.button = Button(button_number)
        self.destruction_wating_time = destruction_wating_time

    def fire_and_conveyor(self):
        self.button.wait_for_press()
        self.fire_and_conveyor()
        sleep(self.destruction_wating_time)

    def fire_truck_and_conveyor(self):
        siren_fig = 32
        led_time = 12 / siren_fig

        mixer.init()
        mixer.music.load(self.siren_mp3_path)  # 12sec
        mixer.music.play(1)
        for i in range(siren_fig):
            self.led_siren.on()
            sleep(led_time)
            self.led_siren.off()
            sleep(led_time)
        mixer.music.stop()

    def conveyor(self):
        pass


if __name__ == "__main__":
    print("start")
    fac = FireAndConveyor("../../MP2_A2_audiofiles/AudioFiles",
                          3, 3, 3, 3)
    fac.fire_and_conveyor()
    print("END")
