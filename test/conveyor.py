#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:36:10 2018

@author: crantu
"""

from tb6612fng import TB6612FNG
from read_pincfg import ReadPinFig
from read_freqcfg import ReadFreqFig
from test_conveyor import MeasureConveyorTime

pin_fig = ReadPinFig()
freq_fig = ReadFreqFig()


class Conveyor:
    def __init__(self):
        self.motor_moveconv = TB6612FNG(pin_fig_in1=pin_fig.moveconv_motorin1,
                                        pin_fig_in2=pin_fig.moveconv_motorin2,
                                        pin_fig_pwm=pin_fig.moveconv_motorpwm,
                                        frequency=None)

    def on(self):
        self.motor_moveconv.cw()
        print("conveyor on")

    def off(self):
        self.motor_moveconv.stop_and_close()
        print("conveyor off")


if __name__ == "__main__":
    conveyor = Conveyor()
    mct = MeasureConveyorTime(conveyor)
