#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:29:47 2018

@author: crantu
"""
from pygame import mixer
from gpiozero import LED
from os import path


class Explode:
    def __init__(self, led_explode_pin, audiofiles_dir):
        self.led_explode = LED(led_explode_pin)
        self.mixer_explode = mixer
        self.audiofiles_dir = audiofiles_dir

    def on(self):
        siren_mp3_path = path.join(self.audiofiles_dir, "bomb1.mp3")
        self.mixer_explode.init()
        self.mixer_explode.music.load(siren_mp3_path)
        self.mixer_explode.music.play(1)
        self.led_explode.blink()
        print("siren on")

    def off(self):
        self.mixer_explode.music.stop()
        self.led_explode.off()
        print("siren off")


if __name__ == "__main__":
    from read_setting_json import Setting
    from time import sleep
    pin_fig = Setting("pin")
    setting_time = Setting("time")
    explode = Explode(int(pin_fig.setting_json["led"]["describe_explosion"]),
                      "../../MP2_A2_audiofiles/AudioFiles/")
    explode.on()
    sleep(int(setting_time.setting_json["explode_and_escape"]
                                   ["describe_explosion"]["operation_time"]))
    explode.off()
