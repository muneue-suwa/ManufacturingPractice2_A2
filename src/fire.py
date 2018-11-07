#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:34:15 2018

@author: crantu
"""

from gpiozero import LED


class Fire:
    def __init__(self, led_fire_pin):
        self.led_fire = LED(led_fire_pin)

    def on(self):
        self.led_fire.blink()
        print("fire on")

    def off(self):
        self.led_fire.off()
        print("fire off")


if __name__ == "__main__":
    from read_setting_json import Setting
    from time import sleep
    pin_fig = Setting("pin")
    setting_time = Setting("time")
    fire = Fire(int(pin_fig.setting_json["led"]["describe_fire"]))
    fire.on()
    sleep(float(setting_time.setting_json["fire_and_conveyor"]
                      ["describe_fire"]["operation_time"]))
    fire.off()
