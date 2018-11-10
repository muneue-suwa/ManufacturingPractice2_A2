#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:33:02 2018

@author: crantu
"""

from time import sleep, time


class DelayAndRun:
    def __init__(self, init_time=None):
        self.start_time = time()
        self.init_time = init_time

    def delay_and_run(self, func, wating_time, before_execution_time):
        wating_time -= before_execution_time
        if wating_time > 0:
            sleep(wating_time)

        old_time = time()
        if self.init_time:
            print("{:.2f}, ".format(old_time - self.init_time), end="")
        else:
            print("None, ", end="")
        print("{:.2f} [sec]: ".format(old_time - self.start_time), end="")
        func()
        new_execution_time = time() - old_time

        return new_execution_time


if __name__ == "__main__":
    def helloworld():
        print("hello world!")
    dar = DelayAndRun()
    delay_and_run = dar.delay_and_run
    temp = delay_and_run(func=helloworld, wating_time=2,
                         before_execution_time=0)
    temp = delay_and_run(func=helloworld, wating_time=2,
                         before_execution_time=temp)
    print(temp)
