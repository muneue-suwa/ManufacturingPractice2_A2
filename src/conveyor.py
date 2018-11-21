#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:36:10 2018

@author: crantu
"""

from read_setting_json import Setting
from tb6612fng import TB6612FNG
pin_fig = Setting("pin")


class Conveyor:
    def __init__(self):
        motor_pin_fig_in1 =\
            int(pin_fig.setting_json["motor"]["move_conveyor"]["in1"])
        motor_pin_fig_in2 =\
            int(pin_fig.setting_json["motor"]["move_conveyor"]["in2"])
        self.motor_conveyor = TB6612FNG(pin_fig_in1=motor_pin_fig_in1,
                                        pin_fig_in2=motor_pin_fig_in2)

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
