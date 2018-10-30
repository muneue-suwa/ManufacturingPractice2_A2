#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:56:58 2018

@author: crantu
"""

from gpiozero import Button

import src.fire_and_conveyor
import src.explode_and_escapse

fc = src.fire_and_conveyor.FireAndConveyor()
ee = src.explode_and_escape.ExplodeAndEscape()

first_button = Button(3)
second_button = Button(4)


def main():
    first_button.wait_for_press()
    fc.fire_and_conveyor()

    second_button.wait_for_press()
    ee.explode_and_escape()


if __name__ == "__main__":
    main()
