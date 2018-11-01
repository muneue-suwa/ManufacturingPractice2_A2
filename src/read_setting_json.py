#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:55:50 2018

@author: crantu
"""

import json

from pprint import pprint

import os
from os import path
os.chdir(path.dirname(path.abspath(__file__)))


class Setting:
    def __init__(self, mode):
        if mode == "time":
            json_filename = "setting_time.json"
        elif mode == "pin" or mode == "pin_fig":
            json_filename = "setting_pin_fig.json"
        else:
            raise ValueError("'mode' of Setting must be time or pin")
        self.setting_json = self.json_to_dict(json_filename)

    def json_to_dict(self, json_filename):
        setting_file_dir = "~/Git/ManufacturingPractice2_A2/setting_files"
        with open(path.join(path.expanduser(setting_file_dir), json_filename),
                  "r") as f:
            setting_data = json.load(f)
        return setting_data

# {'encrypt': {'input': ['~/my_alias', '~/.bashrc'], 'output': '~/'},
#  'key': {'public_key': 'key/public_key', 'secret_key': 'key/secret_key'}}


if __name__ == "__main__":
    setting = Setting("pin")
    pprint(setting.setting_json)
