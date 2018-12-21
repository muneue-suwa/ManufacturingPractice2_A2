#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:56:58 2018

@author: crantu
"""

from gpiozero import Button, LED
from os import path
from argparse import ArgumentParser
from time import time, sleep

from fire_and_conveyor import FireAndConveyor
from explode_and_escape import ExplodeAndEscape
from fire import Fire

from read_pincfg import ReadPinFig
pin_fig = ReadPinFig()


def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('-t', '--finishtime', type=bool,
                           default=False,
                           help='Measure finish time')
    argparser.add_argument('-e', '--waitforenter', type=bool,
                           default=False,
                           help='Wait for ENTER key instead of button press')
    argparser.add_argument('-l', '--loop', type=bool,
                           default=True)
    return argparser.parse_args()


def main():
    audiodir = path.expanduser('~/Git/MP2_A2_audiofiles/AudioFiles')
    fire = Fire("Arduino")
    fc = FireAndConveyor(audiofiles_dir=audiodir)
    ee = ExplodeAndEscape(audiofiles_dir=audiodir)

    first_button = Button(pin_fig.first_button)
    second_button = Button(pin_fig.second_button)
    main_status_led = LED(pin_fig.status_led_2)
    recovery_staus_led = LED(pin_fig.status_led_1)

    option = get_option()

    main_status_led.on()
    print("start")

    if option.waitforenter:
        input("Waiting for ENTER key instead of BUTTON1: ")
    else:
        print("Waiting for BUTTON1 press")
        first_button.wait_for_press()
    main_status_led.blink()
    init_time = time()
    fire.on()
    fc.main(init_time)

    if option.waitforenter:
        input("Waiting for ENTER key instead of BUTTON2: ")
    else:
        second_button.wait_for_press()
        print("Waiting for BUTTON2 press")
    ee.main(init_time)
    sleep(5)
    fire.off()

    if option.finishtime:
        input("Press ENTER key to measure finish time: ")
        print("{:.3f} sec: ".format(time() - init_time), end="")
    main_status_led.off()
    print("end")

    if option.loop is True:
        main()


if __name__ == "__main__":
    main()
