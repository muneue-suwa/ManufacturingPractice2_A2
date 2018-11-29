#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:32:36 2018

@author: crantu
"""

from gpiozero import LED
from read_pincfg import ReadPinFig
pin_fig = ReadPinFig()


class Escape:
    def __init__(self):
        self.motor_escape = LED(pin_fig.escape_relayswitch)

    def on(self):
        self.motor_escape.on()
        print("escape on")

    def off(self):
        self.motor_escape.off()
        print("escape off")


if __name__ == "__main__":
    from time import sleep
    from read_setting_json import Setting
    setting_time = Setting("time")
    escape = Escape()
    escape.on()
    sleep(float(setting_time.setting_json["explode_and_escape"]
                                         ["launch_balls"]
                                         ["operation_time"]))
    escape.off()
