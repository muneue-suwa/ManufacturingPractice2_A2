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
fc = FireAndConveyor(led_siren_pin=int(led_pin["describe_fire_truck"]),
                     audiofiles_dir=audiodir,
                     motor_conveyor_pin=int(motor_pin["move_conveyor"]),
                     led_fire_pin=int(led_pin["describe_fire"]))
ee = ExplodeAndEscape(led_explode_pin=int(led_pin["describe_explosion"]),
                      audiofiles_dir=audiodir,
                      motor_escape_pin=int(motor_pin["launch_balls"]))


button_pin = pinfig.setting_json["button"]
first_button = Button(int(button_pin["first_button"]))
second_button = Button(int(button_pin["second_button"]))


def main():
    first_button.wait_for_press()
    fc.main()

    second_button.wait_for_press()
    ee.main()


if __name__ == "__main__":
    main()
