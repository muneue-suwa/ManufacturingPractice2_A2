#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:32:34 2018

@author: crantu
"""

from siren import Siren
from conveyor import Conveyor
from fire import Fire
from destroy_coveyor import DestroyCoveyor
from remove_stopper import RemoveStopper

from time_calculator import fire_and_conveyor_time
from sort_functions import SortFunctions
from delay_and_run import DelayAndRun
from read_setting_json import Setting
pin_fig = Setting("pin")


class FireAndConveyor:
    def __init__(self, audiofiles_dir):

        self.siren = Siren(audiofiles_dir)
        self.conveyor = Conveyor()
        self.fire = Fire()
        self.destroy_conveyor = DestroyCoveyor()  # temp
        self.remove_stopper = RemoveStopper()  # temp

        sorted_items, self.wating_times = fire_and_conveyor_time()

        print(sorted_items)
        func_dict = {'describe_fire_start': self.fire.on,
                     'describe_fire_end': self.fire.off,
                     'describe_fire_truck_start': self.siren.on,
                     'describe_fire_truck_end': self.siren.off,
                     'move_conveyor_start': self.conveyor.on,
                     'move_conveyor_end': self.conveyor.off,
                     'destroy_coveyor_start': self.destroy_conveyor.on,
                     'destroy_coveyor_end': self.destroy_conveyor.off,
                     'remove_stopper_start': self.remove_stopper.on,
                     'remove_stopper_end': self.remove_stopper.off}

        sortfunc = SortFunctions(sorted_items, func_dict)
        self.func = sortfunc.func

    def main(self, init_time=None):
        temp_execution_time = 0.0
        dar = DelayAndRun(init_time)
        for i in range(len(self.func)):
            temp_execution_time =\
                dar.delay_and_run(func=self.func[i],
                                  wating_time=self.wating_times[i],
                                  before_execution_time=temp_execution_time)


if __name__ == "__main__":
    fc = FireAndConveyor(audiofiles_dir="../../MP2_A2_audiofiles/AudioFiles")
    fc.main()
