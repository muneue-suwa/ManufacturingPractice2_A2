#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:32:34 2018

@author: crantu
"""

from pygame import mixer
from gpiozero import LED
from time import sleep, time
from os import path

# audiofiles_dir = "../../MP2_A2_audiofiles/"
# siren_mp3 = "ambulance-siren2.mp3"


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
