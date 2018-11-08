#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:36:10 2018

@author: crantu
"""

from gpiozero import LED
from .read_setting_json import Setting
pin_fig = Setting("pin")


class Conveyor:
    def __init__(self):
        self.motor_conveyor =\
            LED(int(pin_fig.setting_json["motor"]
                                        ["move_conveyor"]))

    def on(self):
        self.motor_conveyor.on()
        print("conveyor on")

    def off(self):
        self.motor_conveyor.off()
        print("conveyor off")


if __name__ == "__main__":
    from time import sleep
    setting_time = Setting("time")
    conveyor = Conveyor()
    conveyor.on()
    sleep(float(setting_time.setting_json["fire_and_conveyor"]
                                         ["move_conveyor"]
                                         ["operation_time"]))
    conveyor.off()
