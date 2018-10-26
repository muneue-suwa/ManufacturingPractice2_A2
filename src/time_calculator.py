#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:56:09 2018

@author: crantu
"""

from pprint import pprint
from read_setting_json import Setting
setting = Setting()
setting_file = setting.setting_json


def fire_and_conveyor_time():
    times = {'describe_fire': {'start': 0.0, 'end': 0.0},
             'describe_fire_truck': {'start': 0.0, 'end': 0.0},
             'move_conveyor': {'start': 0.0, 'end': 0.0},
             'destroy_coveyor': {'start': 0.0, 'end': 0.0},
             'destroy_crane_time': {'start': 0.0, 'end': 0.0},
             'remove_stopper': {'start': 0.0, 'end': 0.0}}

    # setting_times = setting_file['fire_and_conveyor']

    for setting_times in setting_file['fire_and_conveyor']:
        times[setting_times]['start'] =\
            float(setting_file['fire_and_conveyor']
                  [setting_times]['beginning_time'])
        times[setting_times]['end'] =\
            float(setting_file['fire_and_conveyor']
                  [setting_times]['beginning_time'])\
            + float(setting_file['fire_and_conveyor']
                    [setting_times]['operation_time'])

    return times


"""
{'explode_and_escape': {'describe_explosion': {'beginning time': '',
                                               'operation time': ''},
                        'launch_balls': {'beginning time': '',
                                         'operation time': ''}},
 'fire_and_conveyor': {'describe_fire': {'beginning time': '',
                                         'operation time': ''},
                       'describe_fire_truck': {'beginning time': '',
                                               'operation time': ''},
                       'destroy_coveyor': {'beginning time': '',
                                           'operation time': ''},
                       'destroy_crane_time': {'beginning time': '',
                                              'operation time': ''},
                       'move_conveyor': {'beginning time': '',
                                         'operation time': ''},
                       'remove_stopper': {'beginning time': '',
                                          'operation time': ''}}}
"""


if __name__ == "__main__":
    setting = Setting()
    pprint(fire_and_conveyor_time())
