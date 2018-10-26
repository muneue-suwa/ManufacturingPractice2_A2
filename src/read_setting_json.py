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


def json_to_dict():
    with open("../setting.json", "r") as f:
        setting_data = json.load(f)

    return setting_data

# {'encrypt': {'input': ['~/my_alias', '~/.bashrc'], 'output': '~/'},
#  'key': {'public_key': 'key/public_key', 'secret_key': 'key/secret_key'}}


if __name__ == "__main__":
    pprint(json_to_dict())
