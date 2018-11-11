#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:55:19 2018

@author: crantu
"""

from read_setting_json import Setting
pin_fig = Setting("pin")


class RemoveStopper:
    def __init__(self):
        # pin_fig.setting_json["motor"]["remove_stopper"]
        pass

    def on(self):
        print("remove stopper on")

    def off(self):
        print("remove stopper off")


if __name__ == "__main__":
    from time import sleep
    setting_time = Setting("time")
    sleep(float(setting_time.setting_json["fire_and_conveyor"]
                                         ["remove_stopper"]
                                         ["operation_time"]))
