#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 09:09:06 2018

@author: wincrantu
"""

from time import sleep, time


def MeasureConveyorTime(conveyor_class):
    # init_time = time()
    print("Press ENTER key and start to measure time of conveyor")
    input("If you want to stop, press Ctrl+C: ")
    try:
        init_time = time()
        conveyor_class.on()
        sleep(60)
    except KeyboardInterrupt:
        print("time: {}".format(time() - init_time))
    finally:
        conveyor_class.off()
