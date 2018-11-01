#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:33:02 2018

@author: crantu
"""

from time import sleep, time


class DelayAndRun:
    def __init__(self):
        self.start_time = time()

    def delay_and_run(self, func, wating_time, before_execution_time):
        if wating_time - before_execution_time > 0:
            sleep(wating_time - before_execution_time)

        old_time = time()
        print("{:.3f} sec: ".format(time() - self.start_time), end="")
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
