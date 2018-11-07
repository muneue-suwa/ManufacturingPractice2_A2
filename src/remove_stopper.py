#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:55:19 2018

@author: crantu
"""


class RemoveStopper:
    def __init__(self):
        pass

    def on(self):
        print("remove stopper on")

    def off(self):
        print("remove stopper off")


if __name__ == "__main__":
    from read_setting_json import Setting
    from time import sleep
    pin_fig = Setting("pin")
    setting_time = Setting("time")
    pin_fig.setting_json["motor"]["remove_stopper"]
    sleep(setting_time.setting_json["fire_and_conveyor"]
                                   ["remove_stopper"]["operation_time"])
