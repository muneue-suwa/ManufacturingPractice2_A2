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


class MP2_A2:
    def __init__(self):
        # Preparing
        self.audiodir = path.expanduser('~/Git/MP2_A2_audiofiles/AudioFiles')
        self.fire = Fire("Arduino")
        self.first_button = Button(pin_fig.first_button)
        self.second_button = Button(pin_fig.second_button)
        self.main_status_led = LED(pin_fig.status_led_2)
        self.recovery_staus_led = LED(pin_fig.status_led_1)

        self.get_option()

    def get_option(self):
        argparser = ArgumentParser()
        argparser.add_argument('-t', '--finishtime', action='store_true',
                               help='Measure finish time')
                                # default is False
        argparser.add_argument('-e', '--waitforenter', action='store_true',
                               help=('Wait for ENTER key '
                                     'instead of button press'))
                                # default is False
        argparser.add_argument('-nl', '--no-loop', action='store_true',
                               help='Loop this script')
                                # default is False
        self.option = argparser.parse_args()

    def move_robot(self):
        # Preparing
        self.fc = FireAndConveyor(audiofiles_dir=self.audiodir)
        self.ee = ExplodeAndEscape(audiofiles_dir=self.audiodir)
        # Move Robot
        self.main_status_led.on()

        if self.option.waitforenter:
            input("Waiting for ENTER key instead of BUTTON1 (first section): ")
        else:
            print("Waiting for BUTTON1 press (first section)")
            self.first_button.wait_for_press()

        print("move_robot start")
        self.main_status_led.blink(on_time=1, off_time=2)
        init_time = time()
        self.fire.on()
        self.fc.main(init_time)

        self.main_status_led.blink(on_time=0.5, off_time=0.5)
        if self.option.waitforenter:
            input("Waiting for ENTER key instead of BUTTON2 (second section): ")
        else:
            print("Waiting for BUTTON2 press (second section)")
            self.second_button.wait_for_press()

        self.main_status_led.blink(on_time=1, off_time=2)
        self.ee.main(init_time)
        sleep(1)
        self.fire.off()
        print("move_robot end")

        if self.option.finishtime:
            input("Press ENTER key to measure finish time: ")
            print("{:.3f} sec: ".format(time() - init_time), end="")
        self.main_status_led.off()

    def recovery_robot(self):
        # Preparing
        self.recovery = Recovery()
        # Recovery Robot
        sleep_time = 0.1

        self.recovery_staus_led.on()
        print("Waiting for BUTTON1 press (recovery section)")
        self.first_button.wait_for_press()
        press_button_time = 0
        while self.first_button.is_pressed:
            press_button_time += 1
            if press_button_time >= 2.0 / sleep_time:
                self.recovery_staus_led.off()
            sleep(sleep_time)
        if press_button_time < 2 / sleep_time:
            print("recovery_robot start")
            self.recovery_staus_led.blink(on_time=1, off_time=2)
            self.recovery.main()
            print("recovery_robot end")
            self.recovery_staus_led.off()
        else:
            print("recovery was skipped")

    def main(self):
        self.move_robot()
        self.recovery_robot()
        # Start main() again for loop
        if not self.option.no_loop:
            self.main()


if __name__ == "__main__":
    mp2_a2 = MP2_A2()
    mp2_a2.main()
