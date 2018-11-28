#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:05:46 2018

@author: wincrantu
"""

import configparser
from os import path

config = configparser.RawConfigParser()
setting_file_dir = "~/Git/ManufacturingPractice2_A2/setting_files"
config.read(path.join(path.expanduser(setting_file_dir), "pin.cfg"))

an_int = config.getint("siren", "led")
print(an_int)


class FIRE:
    def __init__(self):
        self.led = config.getint("fire", "led")
