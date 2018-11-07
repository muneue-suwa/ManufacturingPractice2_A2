#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:56:58 2018

@author: crantu
"""

from gpiozero import Button

import src.fire_and_conveyor
import src.explode_and_escape
import src.read_setting_json

fc = src.fire_and_conveyor.FireAndConveyor()
ee = src.explode_and_escape.ExplodeAndEscape()
pinfig = src.read_setting_json.Setting("pin_fig")

button_pin = pinfig.setting_json["button"]
first_button = Button(button_pin["first_button"])
second_button = Button(button_pin["second_button"])


def main():
    first_button.wait_for_press()
    fc.fire_and_conveyor()

    second_button.wait_for_press()
    ee.explode_and_escape()


if __name__ == "__main__":
    main()
