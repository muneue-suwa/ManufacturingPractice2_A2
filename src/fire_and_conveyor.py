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
conveyour_number = 18
button_number = 3


class FireAndConveyor:
    def __init__(self,
                 audiofiles_dir,
                 siren_led_pin_number,
                 conveyour_pin_number):
        self.siren = Siren(LED(siren_led_pin_number))
        self.conveyor = Conveyor(LED(conveyour_number))

    class Conveyor:
        def __init__(self):
            self.on = self.conveyor.on
            self.off = self.conveyor.off

    class Siren(self):
        pass

class Conveyor:
    def __init__(self, motor_conveyor):
        self.motor_conveyor = motor_conveyor
        self.on = self.motor_conveyor.on
        self.off = self.motor_conveyor.off


class Siren:
    def __init__(self, led_siren, audiofiles_dir):
        self.led_siren = led_siren
        self.mixer_siren = mixer
        self.audiofiles_dir = audiofiles_dir

    def on(self):
        siren_mp3_path = path.join(self.audiofiles_dir, "ambulance-siren2.mp3")
        self.mixer_siren.init()
        self.mixer_siren.music.load(siren_mp3_path)  # 12sec
        self.mixer_siren.music.play(-1)
        self.led_siren.blink()

    def off(self):
        self.mixer_siren.music.stop()
        self.led_siren.off()

if __name__ == "__main__":
    print("start")
    fac = FireAndConveyor("../../MP2_A2_audiofiles/AudioFiles",
                          3, 3, 3, 3)
    fac.fire_and_conveyor()
    print("END")
