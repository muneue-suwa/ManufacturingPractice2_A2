#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:36:10 2018

@author: crantu
"""

from tb6612fng import TB6612FNG
from read_pincfg import ReadPinFig
pin_fig = ReadPinFig()


class Conveyor:
    def __init__(self):
        self.motor_moveconv = TB6612FNG(pin_fig_in1=pin_fig.moveconv_motorin1,
                                        pin_fig_in2=pin_fig.moveconv_motorin2,
                                        pin_fig_pwm=pin_fig.moveconv_motorpwm)

    def on(self):
        self.motor_moveconv.cw()
        print("conveyor on")

    def off(self):
        self.motor_moveconv.stop_and_close()
        print("conveyor off")


if __name__ == "__main__":
    from time import sleep
    from read_setting_json import Setting
    setting_time = Setting("time")
    conveyor = Conveyor()
    conveyor.on()
    sleep(float(setting_time.setting_json["fire_and_conveyor"]
                                         ["move_conveyor"]
                                         ["operation_time"]))
    conveyor.off()
