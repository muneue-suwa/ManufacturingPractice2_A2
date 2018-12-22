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


class Recovery:
    def __init__(self):
        pass

    def main(self):
        conveyor = Conveyor()
        destroy_conveyor = DestroyCoveyor()
        remove_stopper = RemoveStopper()

        self.motor_moveconv = conveyor.motor_moveconv
        self.motor_destconv = destroy_conveyor.motor_destconv
        self.servo = remove_stopper.servo

        print("START motor_destconv initializing")
        self.motor_destconv.ccw()
        sleep(float(setting_time.setting_json["fire_and_conveyor"]
                                             ["destroy_coveyor"]
                                             ["operation_time"]))
        self.motor_destconv.stop_and_close()
        print("END motor_destconv initializing")

        print("START motor_moveconv initializing")
        self.motor_moveconv.ccw()
        sleep(float(setting_time.setting_json["fire_and_conveyor"]
                                             ["move_conveyor"]
                                             ["operation_time"]))
        self.motor_moveconv.stop_and_close()
        print("END motor_moveconv initializing")

        print("START stopper initializing")
        self.servo.min()
        sleep(1)
        self.servo.close()
        print("END stopper initializing")


if __name__ == "__main__":
    recovery = Recovery()
    recovery.main()
