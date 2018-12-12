#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:34:15 2018

@author: crantu
"""

from gpiozero import LED, DigitalOutputDevice
from read_pincfg import ReadPinFig
pin_fig = ReadPinFig()


class Fire:
    def __init__(self, mode="rpi"):
        if mode == "arduino" or mode == "Arduino":
            self.arduino_fire = DigitalOutputDevice(pin_fig.fire_led)
            self.on = self.arduino_fire_on_off
            self.off = self.arduino_fire_on_off
        else:
            self.led_fire = LED(pin_fig.fire_led)
            self.on = self.rpi_fire_on
            self.off = self.rpi_fire_off

    def arduino_fire_on_off(self):
        self.arduino_fire.on()
        sleep(0.4)
        self.arduino_fire.off()
        # self.arduino_fire.close()

    def rpi_fire_on(self):
        self.led_fire.blink(on_time=0.1, off_time=0.1)
        print("fire on")

    def rpi_fire_off(self):
        self.led_fire.off()
        print("fire off")


if __name__ == "__main__":
    from time import sleep
    from read_setting_json import Setting
    setting_time = Setting("time")
    fire = Fire("Arduino")
    fire.on()
    # sleep(float(setting_time.setting_json["fire_and_conveyor"]
    #                                      ["describe_fire"]
    #                                      ["operation_time"]))
    sleep(10)
    fire.off()
