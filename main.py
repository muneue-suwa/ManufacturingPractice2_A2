#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:56:58 2018

@author: crantu
"""

from gpiozero import Button
from os import path

from src.fire_and_conveyor import FireAndConveyor
from src.explode_and_escape import ExplodeAndEscape
from src.read_setting_json import Setting as mp2Setting

audiodir = path.expanduser('~/Git/MP2_A2_audiofiles/AudioFiles')
pinfig = mp2Setting("pin_fig")
led_pin = pinfig.setting_json["led"]
motor_pin = pinfig.setting_json["motor"]
button_pin = pinfig.setting_json["button"]

fc = FireAndConveyor(audiofiles_dir=audiodir)
ee = ExplodeAndEscape(audiofiles_dir=audiodir)

first_button = Button(int(button_pin["first_button"]))
second_button = Button(int(button_pin["second_button"]))


def main():
    first_button.wait_for_press()
    fc.main()

    second_button.wait_for_press()
    ee.main()


if __name__ == "__main__":
    main()
