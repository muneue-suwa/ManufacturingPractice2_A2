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
    def __init__(self, pin_fig_in1, pin_fig_in2, pin_fig_pwm=None):
        self.in1 = DigitalOutputDevice(pin=pin_fig_in1)
        self.in2 = DigitalOutputDevice(pin=pin_fig_in2)
        if pin_fig_pwm:  # PWM mode
            self.pwm = PWMOutputDevice(pin=pin_fig_pwm)
            self.cw = self.pwm_cw
            self.ccw = self.pwm_ccw
            self.stop = self.pwm_stop
            self.stop_and_close = self.pwm_stop_and_close
        else:
            self.cw = self.digital_cw
            self.ccw = self.digital_ccw
            self.stop = self.digital_stop
            self.stop_and_close = self.digital_stop_and_close

    def digital_cw(self):
        self.in1.on()
        self.in2.off()

    def digital_ccw(self):
        self.in1.off()
        self.in2.on()

    def digital_stop(self):
        self.in1.off()
        self.in2.off()

    def digital_stop_and_close(self):
        self.digital_stop()
        self.in1.close()
        self.in2.close()

    def pwm_cw(self):
        self.pwm.on()
        self.digital_cw()

    def pwm_ccw(self):
        self.pwm.on()
        self.digital_ccw()

    def pwm_stop(self):
        self.pwm.off()
        self.digital_stop()

    def pwm_stop_and_close(self):
        self.pwm_stop()
        self.in1.close()
        self.in2.close()
        self.pwm.close()

    def cw(self):
        pass

    def cww(self):
        pass

    def stop(self):
        pass

    def stop_and_close(self):
        pass


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
