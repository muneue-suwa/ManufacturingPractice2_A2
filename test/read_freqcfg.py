#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:13:16 2018

@author: crantu
"""

import configparser
from os import path


class ReadFreqFig:
    def __init__(self):
        config = configparser.RawConfigParser()
        setting_file_dir = "~/Git/ManufacturingPractice2_A2/setting_files"
        config.read(path.join(path.expanduser(setting_file_dir),
                              "frequency.cfg"))
        self.moveconv_frequency =\
            config.getint("move_conveyor", "frequency")
        self.destconv_frequency =\
            config.getint("destroy_conveyor", "frequency")

    def show(self):
        print("self.moveconv_frequency: {}".format(self.moveconv_frequency))
        print("self.destconv_frequency: {}".format(self.destconv_frequency))


if __name__ == "__main__":
    rpg = ReadFreqFig()
    rpg.show()
