#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:48:40 2018

@author: crantu
"""

from .explode import Explode
from .escape import Escape

from .time_calculator import explode_and_escape_time
from .sort_functions import SortFunctions

from .delay_and_run import DelayAndRun


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
        temp_execution_time = 0.0
        dar = DelayAndRun()
        for i in range(len(self.func)):
            temp_execution_time =\
                dar.delay_and_run(func=self.func[i],
                                  wating_time=self.wating_times[i],
                                  before_execution_time=temp_execution_time)


if __name__ == "__main__":
    from read_setting_json import Setting
    pin_fig = Setting("pin")
    ee =\
        ExplodeAndEscape(int(pin_fig.setting_json["led"]
                                                 ["describe_explosion"]),
                         "../../MP2_A2_audiofiles/AudioFiles",
                         int(pin_fig.setting_json["motor"]
                                                 ["describe_explosion"]))
    ee.main()
