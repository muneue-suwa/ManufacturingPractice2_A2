#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:45:25 2018

@author: crantu
"""

from time import sleep

from gpiozero import Servo
from tb6612fng import TB6612FNG
from read_pincfg import ReadPinFig
from read_freqcfg import ReadFreqFig
from read_setting_json import Setting

pin_fig = ReadPinFig()
freq_fig = ReadFreqFig()
setting_time = Setting("time")


class Recovery:
    def __init__(self):
        self.motor_moveconv = TB6612FNG(pin_fig_in1=pin_fig.moveconv_motorin1,
                                        pin_fig_in2=pin_fig.moveconv_motorin2,
                                        pin_fig_pwm=pin_fig.moveconv_motorpwm,
                                        frequency=freq_fig.moveconv_frequency)

        self.motor_destconv = TB6612FNG(pin_fig_in1=pin_fig.destconv_motorin1,
                                        pin_fig_in2=pin_fig.destconv_motorin2,
                                        pin_fig_pwm=pin_fig.destconv_motorpwm,
                                        frequency=freq_fig.destconv_frequency)

    def main(self):
        self.motor_moveconv.ccw()
        print("START motor_moveconv.ccw()")
        sleep(float(setting_time.setting_json["fire_and_conveyor"]
                                             ["move_conveyor"]
                                             ["operation_time"]))
        self.motor_moveconv.stop_and_close()
        print("END motor_moveconv.ccw()")
        self.motor_destconv.ccw()
        print("START motor_destconv.ccw()")
        sleep(float(setting_time.setting_json["fire_and_conveyor"]
                                             ["destroy_coveyor"]
                                             ["operation_time"]))
        self.motor_destconv.stop_and_close()
        print("END motor_destconv.ccw()")
        print("START stopper recovery")
        self.servo = Servo(pin_fig.remove_stopperservo)
        self.servo.min()
        sleep(1)
        print("END stopper recovery")


if __name__ == "__main__":
    recovery = Recovery()
    recovery.main()
