#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:56:58 2018

@author: crantu
"""

from gpiozero import Button
from os import path
from argparse import ArgumentParser
from time import time

from fire_and_conveyor import FireAndConveyor
from explode_and_escape import ExplodeAndEscape
from read_setting_json import Setting as mp2Setting


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

    print("start")

    if option.waitforenter:
        input("Waiting for ENTER key instead of BUTTON1: ")
    else:
        print("Waiting for BUTTON1 press")
        first_button.wait_for_press()
    init_time = time()
    fc.main(init_time)

    if option.waitforenter:
        input("Waiting for ENTER key instead of BUTTON2: ")
    else:
        second_button.wait_for_press()
        print("Waiting for BUTTON2 press")
    ee.main(init_time)

    if option.finishtime:
        input("Press ENTER key to measure finish time: ")
        print("{:.3f} sec: ".format(time() - init_time), end="")

    print("end")


if __name__ == "__main__":
    main()
