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
from recovery import Recovery

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
    # Preparing
    audiodir = path.expanduser('~/Git/MP2_A2_audiofiles/AudioFiles')
    fire = Fire("Arduino")
    fc = FireAndConveyor(audiofiles_dir=audiodir)
    ee = ExplodeAndEscape(audiofiles_dir=audiodir)
    recovery = Recovery()

    first_button = Button(pin_fig.first_button)
    second_button = Button(pin_fig.second_button)
    main_status_led = LED(pin_fig.status_led_2)
    recovery_staus_led = LED(pin_fig.status_led_1)

    option = get_option()

    # Main
    main_status_led.on()

    if option.waitforenter:
        input("Waiting for ENTER key instead of BUTTON1: ")
    else:
        print("Waiting for BUTTON1 press")
        first_button.wait_for_press()

    print("Main start")
    main_status_led.blink()
    init_time = time()
    fire.on()
    fc.main(init_time)

    if option.waitforenter:
        input("Waiting for ENTER key instead of BUTTON2: ")
    else:
        print("Waiting for BUTTON2 press")
        second_button.wait_for_press()
    ee.main(init_time)
    sleep(5)
    fire.off()
    print("Main end")

    if option.finishtime:
        input("Press ENTER key to measure finish time: ")
        print("{:.3f} sec: ".format(time() - init_time), end="")
    main_status_led.off()

    # Recovery
    recovery_staus_led.on()
    if option.waitforenter:
        input("Waiting for ENTER key instead of BUTTON1: ")
    else:
        print("Waiting for BUTTON1 press")
        first_button.wait_for_press()
    press_button_time = time()

    if option.waitforenter:
        input("Waiting for ENTER key instead of BUTTON1: ")
    else:
        print("Waiting for BUTTON1 release")
        first_button.wait_for_release()

    if (time() - press_button_time) < 1:
        print("Recovery start")
        recovery_staus_led.blink()
        recovery.main()
        print("Recovery end")
    else:
        print("Recovery was skipped")
    recovery_staus_led.off()

    # Start main() again for loop
    if option.loop:
        main()


if __name__ == "__main__":
    main()
