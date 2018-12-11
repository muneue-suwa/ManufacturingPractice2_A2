#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:35:13 2018

@author: crantu
"""

from gpiozero import DigitalOutputDevice, PWMOutputDevice

# DigitalOutputDevice(pin, *, active_high=True,
# initial_value=False, pin_factory=None)


class TB6612FNG:
    def __init__(self, pin_fig_in1, pin_fig_in2, pin_fig_pwm,
                 frequency=None):
        self.in1 = DigitalOutputDevice(pin=pin_fig_in1)
        self.in2 = DigitalOutputDevice(pin=pin_fig_in2)
        if frequency is None:  # Not PWM mode
            self.pwm = DigitalOutputDevice(pin=pin_fig_pwm)
        else:  # PWM mode
            self.pwm = PWMOutputDevice(pin=pin_fig_pwm,
                                       frequency=frequency)

    def cw(self):
        self.pwm.on()
        self.digital_cw()

    def ccw(self):
        self.pwm.on()
        self.digital_ccw()

    def stop(self):
        self.pwm.off()
        self.digital_stop()

    def stop_and_close(self):
        self.pwm_stop()
        self.in1.close()
        self.in2.close()
        self.pwm.close()


if __name__ == "__main__":
    from time import sleep
    input("Check pinout (20, 21, 22) and push ENTER key:")
    tb6612fng = TB6612FNG(20, 21, 22)
    print("cw")
    tb6612fng.cw()
    sleep(10)
    print("ccw")
    tb6612fng.ccw()
    sleep(10)
    print("stop_and_close")
    tb6612fng.stop_and_close()
