#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:35:37 2018

@author: crantu
"""

from pygame import mixer
from gpiozero import LED
from os import path
from read_pincfg import ReadPinFig
pin_fig = ReadPinFig()


class Siren:
    def __init__(self, audiofiles_dir):
        self.led_siren = LED(pin_fig.siren_led)
        self.mixer_siren = mixer
        self.audiofiles_dir = audiofiles_dir

    def on(self):
        siren_mp3_path = path.join(self.audiofiles_dir,
                                   "ambulance-siren2.mp3")
        self.mixer_siren.init()
        self.mixer_siren.music.load(siren_mp3_path)  # 12sec
        self.mixer_siren.music.play(-1)
        self.led_siren.blink(on_time=1, off_time=1)
        print("siren on")

    def off(self):
        self.mixer_siren.music.stop()
        self.led_siren.off()
        self.led_siren.close()
        print("siren off")


if __name__ == "__main__":
    from time import sleep
    from read_setting_json import Setting
    setting_time = Setting("time")
    siren = Siren(audiofiles_dir="../../MP2_A2_audiofiles/AudioFiles/")
    siren.on()
    sleep(float(setting_time.setting_json['fire_and_conveyor']
                                         ['describe_fire_truck']
                                         ['operation_time']))
    siren.off()
