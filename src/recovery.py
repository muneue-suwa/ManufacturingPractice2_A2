#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:45:25 2018

@author: crantu
"""

from time import sleep

from read_setting_json import Setting

from conveyor import Conveyor
from destroy_coveyor import DestroyCoveyor
from remove_stopper import RemoveStopper

setting_time = Setting("time")

moveconv = Conveyor()
destconv = DestroyCoveyor()
rmstopper = RemoveStopper()


class Recovery:
    def __init__(self):
        self.motor_moveconv = moveconv.motor_moveconv
        self.motor_destconv = destconv.motor_destconv
        self.servo = rmstopper.servo

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
        self.servo.min()
        sleep(1)
        print("END stopper recovery")


if __name__ == "__main__":
    recovery = Recovery()
    recovery.main()
