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
    times = {'describe_fire_start': 0.0,
             'describe_fire_end': 0.0,
             'describe_fire_truck_start': 0.0,
             'describe_fire_truck_end': 0.0,
             'move_conveyor_start': 0.0,
             'move_conveyor_end': 0.0,
             'destroy_coveyor_start': 0.0,
             'destroy_coveyor_end': 0.0,
             'destroy_crane_time_start': 0.0,
             'destroy_crane_time_end': 0.0,
             'remove_stopper_start': 0.0,
             'remove_stopper_end': 0.0}

    # setting_times = setting_file['fire_and_conveyor']

    for setting_times in setting_file['fire_and_conveyor']:
        times['{}_start'.format(setting_times)] =\
            float(setting_file['fire_and_conveyor']
                  [setting_times]['beginning_time'])
        times['{}_end'.format(setting_times)] =\
            float(setting_file['fire_and_conveyor']
                  [setting_times]['beginning_time'])\
            + float(setting_file['fire_and_conveyor']
                    [setting_times]['operation_time'])

    tmp_old_time = 0.0
    wating_time_list = []
    sorted_item_list = []
    for item, time in sorted(times.items(), key=lambda x: x[1]):
        wating_time_list.append(time - tmp_old_time)
        sorted_item_list.append(item)
        tmp_old_time = time

    return sorted_item_list, wating_time_list


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
