#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:32:36 2018

@author: crantu
"""

from gpiozero import LED
from .read_setting_json import Setting
pin_fig = Setting("pin")


class Escape:
    def __init__(self):
        self.motor_escape = LED(int(pin_fig.setting_json["motor"]
                                                        ["launch_balls"]))

    def on(self):
        self.motor_escape.on()
        print("escape on")

    def off(self):
        self.motor_escape.off()
        print("escape off")


if __name__ == "__main__":
    from time import sleep
    setting_time = Setting("time")
    escape = Escape()
    escape.on()
    sleep(float(setting_time.setting_json["explode_and_escape"]
                                         ["launch_balls"]
                                         ["operation_time"]))
    escape.off()
