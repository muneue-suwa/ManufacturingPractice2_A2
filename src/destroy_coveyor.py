#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:53:09 2018

@author: crantu
"""


class DestroyCoveyor:
    def __init__(self):
        pass

    def on(self):
        print("destroy conveyor on")

    def off(self):
        print("destroy conveyor off")


if __name__ == "__main__":
    from read_setting_json import Setting
    from time import sleep
    setting_time = Setting("time")
    pin_fig = Setting("pin")
    int(pin_fig.setting_json["motor"]["destroy_coveyor"])
    sleep(float(setting_time.setting_json["fire_and_conveyor"]
                                   ["destroy_coveyor"]["operation_time"]))
