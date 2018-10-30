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

# audiofiles_dir = "../../MP2_A2_audiofiles/"
# siren_mp3 = "ambulance-siren2.mp3"


class FireAndConveyor:
    def __init__(self, led_siren_pin, audiofiles_dir,
                 motor_conveyor_pin,
                 led_fire_pin):

        self.siren = Siren(led_siren_pin, audiofiles_dir)
        self.conveyor = Conveyor(motor_conveyor_pin)
        self.fire = Fire(led_fire_pin)
        self.destroy_conveyor = DestroyCoveyor()  # temp
        self.remove_stopper = RemoveStopper()  # temp

        self.sort_functions()

    def sort_functions(self):
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

        self.func = []
        for item in sorted_items:
            self.func.append(func_dict[item])

    def main(self):
        for i in range(len(self.func)):
            self.func[i]
            self.wating_times[i]


if __name__ == "__main__":
    led_siren_pin_fig = 17
    conveyour_pin_fig = 18

    conveyor = Conveyor(conveyour_pin_fig)
    siren = Siren(led_siren_pin_fig, "../../MP2_A2_audiofiles/")

    conveyor.on()
    siren.on()
    sleep(10)
    siren.off()
    conveyor.off()
