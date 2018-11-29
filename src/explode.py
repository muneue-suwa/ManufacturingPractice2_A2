#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:29:47 2018

@author: crantu
"""
from pygame import mixer
from gpiozero import LED
from os import path
from read_pincfg import ReadPinFig
pin_fig = ReadPinFig()


class Explode:
    def __init__(self, audiofiles_dir):
        self.led_explode = LED(pin_fig.explode_led)
        self.mixer_explode = mixer
        self.audiofiles_dir = audiofiles_dir

    def on(self):
        siren_mp3_path = path.join(self.audiofiles_dir, "bomb1.mp3")
        self.mixer_explode.init()
        self.mixer_explode.music.load(siren_mp3_path)
        self.mixer_explode.music.play(1)
        self.led_explode.blink()
        print("explode on")

    def off(self):
        self.mixer_explode.music.stop()
        self.led_explode.off()
        print("explode off")


if __name__ == "__main__":
    from time import sleep
    from read_setting_json import Setting
    setting_time = Setting("time")
    explode = Explode("../../MP2_A2_audiofiles/AudioFiles/")
    explode.on()
    sleep(float(setting_time.setting_json["explode_and_escape"]
                                         ["describe_explosion"]
                                         ["operation_time"]))
    explode.off()
