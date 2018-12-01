#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:34:15 2018

@author: crantu
"""

from gpiozero import LED
from read_pincfg import ReadPinFig
pin_fig = ReadPinFig()


class Fire:
    def __init__(self):
        self.led_fire = LED(pin_fig.fire_led)
        # print(self.led_fire)

    def on(self):
        self.led_fire.blink(on_time=0.1, off_time=0.1)
        print("fire on")

    def off(self):
        self.led_fire.off()
        print("fire off")


if __name__ == "__main__":
    from time import sleep
    from read_setting_json import Setting
    setting_time = Setting("time")
    fire = Fire()
    fire.on()
    # sleep(float(setting_time.setting_json["fire_and_conveyor"]
    #                                      ["describe_fire"]
    #                                      ["operation_time"]))
    sleep(60)
    fire.off()
