#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:48:40 2018

@author: crantu
"""

from time import sleep

from explode import Explode
from escape import Escape

from time_calculator import explode_and_escape_time
from sort_functions import SortFunctions


class ExplodeAndEscape:
    def __init__(self, led_explode_pin, audiofiles_dir,
                 motor_escape_pin):
        self.explode = Explode(led_explode_pin=led_explode_pin,
                               audiofiles_dir=audiofiles_dir)
        self.escape = Escape(motor_escape_pin=motor_escape_pin)
        ######
        sorted_items, self.wating_times = explode_and_escape_time()

        print(sorted_items)

        func_dict = {'describe_explosion_start': self.explode.on,
                     'describe_explosion_end': self.explode.off,
                     'launch_balls_start': self.escape.on,
                     'launch_balls_end': self.escape.off}

        sortfunc = SortFunctions(sorted_items, func_dict)
        self.func = sortfunc.func

    def main(self):
        for i in range(len(self.func)):
            self.func[i]()
            sleep(self.wating_times[i])
