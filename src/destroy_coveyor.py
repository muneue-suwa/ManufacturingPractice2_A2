#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:53:09 2018

@author: crantu
"""

from tb6612fng import TB6612FNG
from read_pincfg import ReadPinFig
pin_fig = ReadPinFig()


class DestroyCoveyor:
    def __init__(self):
        self.motor_destconv = TB6612FNG(pin_fig_in1=pin_fig.destconv_motorin1,
                                        pin_fig_in2=pin_fig.destconv_motorin2,
                                        pin_fig_pwm=pin_fig.destconv_motorpwm)

    def on(self):
        self.motor_destconv.cw()
        print("destroy conveyor on")

    def off(self):
        self.motor_destconv.stop_and_close()
        print("destroy conveyor off")


if __name__ == "__main__":
    from time import sleep
    from read_setting_json import Setting
    setting_time = Setting("time")
    sleep(float(setting_time.setting_json["fire_and_conveyor"]
                                         ["destroy_coveyor"]
                                         ["operation_time"]))
