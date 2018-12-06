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
            pass
        else:
            raise ValueError("'mode' of Setting must be time")
        self.setting_json = self.json_to_dict()

    def json_to_dict(self):
        setting_file_dir = "~/Git/ManufacturingPractice2_A2/setting_files"
        with open(path.join(path.expanduser(setting_file_dir),
                            "setting_time.json"),
                  "r") as f:
            setting_data = json.load(f)
        return setting_data

# {'encrypt': {'input': ['~/my_alias', '~/.bashrc'], 'output': '~/'},
#  'key': {'public_key': 'key/public_key', 'secret_key': 'key/secret_key'}}


if __name__ == "__main__":
    setting = Setting("time")
    pprint(setting.setting_json)
