#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:56:09 2018

@author: crantu
"""

from pprint import pprint
from read_setting_json import Setting
setting_time = Setting("time")
setting_file = setting_time.setting_json


def fire_and_conveyor_time():
    times = {'describe_fire_start': 0.0,
             'describe_fire_end': 0.0,
             'describe_fire_truck_start': 0.0,
             'describe_fire_truck_end': 0.0,
             'move_conveyor_start': 0.0,
             'move_conveyor_end': 0.0,
             'destroy_coveyor_start': 0.0,
             'destroy_coveyor_end': 0.0,
             'remove_stopper_start': 0.0,
             'remove_stopper_end': 0.0}

    return time_calculator_common(times_dict=times,
                                  json_object_key_name='fire_and_conveyor')


def explode_and_escape_time():
    times = {'describe_explosion_start': 0.0,
             'describe_explosion_end': 0.0,
             'launch_balls_start': 0.0,
             'launch_balls_end': 0.0}

    return time_calculator_common(times_dict=times,
                                  json_object_key_name='explode_and_escape')


def time_calculator_common(times_dict, json_object_key_name):
    for setting_times in setting_file[json_object_key_name]:
        times_dict['{}_start'.format(setting_times)] =\
            float(setting_file[json_object_key_name]
                  [setting_times]['beginning_time'])
        times_dict['{}_end'.format(setting_times)] =\
            float(setting_file[json_object_key_name]
                  [setting_times]['beginning_time'])\
            + float(setting_file[json_object_key_name]
                    [setting_times]['operation_time'])

    tmp_old_time = 0.0
    wating_time_list = []
    sorted_item_list = []
    for item, time in sorted(times_dict.items(), key=lambda x: x[1]):
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
    pprint(fire_and_conveyor_time())
