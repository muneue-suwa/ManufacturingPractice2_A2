#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:35:13 2018

@author: crantu
"""

from gpiozero import DigitalOutputDevice

# DigitalOutputDevice(pin, *, active_high=True,
# initial_value=False, pin_factory=None)


class TB6612FNG:
    def __init__(self, pin_fig_in1, pin_fig_in2):
        self.in1 = DigitalOutputDevice(pin=pin_fig_in1)
        self.in2 = DigitalOutputDevice(pin=pin_fig_in2)

    def cw(self):
        self.in1.on()
        self.in2.off()

    def ccw(self):
        self.in1.off()
        self.in2.on()

    def stop(self):
        self.in1.off()
        self.in2.off()

    def stop_and_close(self):
        self.stop()
        self.in1.close()
        self.in2.close()


if __name__ == "__main__":
    from time import sleep
    input("Check pinout (20 and 21) and push ENTER key:")
    tb6612fng = TB6612FNG(20, 21)
    print("cw")
    tb6612fng.cw()
    sleep(10)
    print("ccw")
    tb6612fng.ccw()
    sleep(10)
    print("stop_and_close")
    tb6612fng.stop_and_close()
