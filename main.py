#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:56:58 2018

@author: crantu
"""

from gpiozero import Button
from os import path
from argparse import ArgumentParser

from src.fire_and_conveyor import FireAndConveyor
from src.explode_and_escape import ExplodeAndEscape
from src.read_setting_json import Setting as mp2Setting


def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('-t', '--finishtime', type=bool,
                           default=False,
                           help='Measure finish time')
    argparser.add_argument('-e', '--waitforenter', type=bool,
                           default=False,
                           help='Wait for ENTER key instead of button press')
    return argparser.parse_args()


def main():
    audiodir = path.expanduser('~/Git/MP2_A2_audiofiles/AudioFiles')
    pinfig = mp2Setting("pin_fig")
    button_pin = pinfig.setting_json["button"]

    fc = FireAndConveyor(audiofiles_dir=audiodir)
    ee = ExplodeAndEscape(audiofiles_dir=audiodir)

    first_button = Button(int(button_pin["first_button"]))
    second_button = Button(int(button_pin["second_button"]))

    option = get_option()
    if option.waitforenter:
        input("Waiting ENTER key instead of BUTTON1")
    else:
        first_button.wait_for_press()
    fc.main()

    if option.waitforenter:
        input("Waiting ENTER key instead of BUTTON1")
    else:
        second_button.wait_for_press()
    ee.main()

    if option.finishtime and input("Press ENTER key to measure finish time: "):
        pass

if __name__ == "__main__":
    main()
