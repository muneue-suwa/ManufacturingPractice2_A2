#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:32:36 2018

@author: crantu
"""

from gpiozero import LED


class Escape:
    def __init__(self, motor_escape_pin):
        self.motor_escape = LED(motor_escape_pin)

    def on(self):
        self.motor_escape.on()
        print("escape on")

    def off(self):
        self.motor_escape.off()
        print("escape off")


if __name__ == "__main__":
    from read_setting_json import Setting
    from time import sleep
    pin_fig = Setting("pin")
    setting_time = Setting("time")
    escape =\
        Escape(motor_escape_pin=pin_fig.setting_json["motor"]["launch_balls"])
    escape.on()
    sleep(setting_time["explode_and_escape"]["launch_balls"]["operation_time"])
    escape.off()
