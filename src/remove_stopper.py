#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:55:19 2018

@author: crantu
"""

from gpiozero import Servo
from time import sleep
from read_pincfg import ReadPinFig
pin_fig = ReadPinFig()


class RemoveStopper:
    def __init__(self):
        self.servo = Servo(pin_fig.remove_stopperservo)
        self.servo.min()
        sleep(1)

    def on(self):
        self.servo.value = 0.4
        # sleep(1)
        print("remove stopper on")

    def off(self):
        print("remove stopper off")


if __name__ == "__main__":
    from read_setting_json import Setting
    setting_time = Setting("time")
    rs = RemoveStopper()
    rs.on()
    sleep(float(setting_time.setting_json["fire_and_conveyor"]
                                         ["remove_stopper"]
                                         ["operation_time"]))
    rs.off()
