#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:05:46 2018

@author: wincrantu
"""

import configparser
from os import path


class ReadPinFig:
    def __init__(self):
        config = configparser.RawConfigParser()
        setting_file_dir = "~/Git/ManufacturingPractice2_A2/setting_files"
        config.read(path.join(path.expanduser(setting_file_dir), "pin.cfg"))
        self.fire_led = config.getint("fire", "led")
        self.siren_led = config.getint("siren", "led")
        self.moveconv_motorin1 =\
            config.getint("move_conveyor", "dc_motor_in1")
        self.moveconv_motorin2 =\
            config.getint("move_conveyor", "dc_motor_in2")
        self.moveconv_motorpwm =\
            config.getint("move_conveyor", "dc_motor_pwm")
        self.destconv_motorin1 =\
            config.getint("destroy_conveyor", "dc_motor_in1")
        self.destconv_motorin2 =\
            config.getint("destroy_conveyor", "dc_motor_in2")
        self.destconv_motorpwm =\
            config.getint("destroy_conveyor", "dc_motor_pwm")
        self.remove_stopperservo =\
            config.getint("remove_stopper", "servo_motor")
        self.escape_relayswitch = config.getint("escape", "relay_switch")
        self.explode_led = config.getint("explode", "led")
        self.explode_temp1 = config.getint("explode", "temp_pin_fig_1")
        self.explode_temp2 = config.getint("explode", "temp_pin_fig_2")
        self.first_button = config.getint("button", "first_button")
        self.second_button = config.getint("button", "second_button")
        self.shutdown_button = config.getint("shutdown_button",
                                              "shutdown_button")
        self.boot_led = config.getint("shutdown_button", "boot_led")

    def show(self):
        print("self.fire_led: {}".format(self.fire_led))
        print("self.siren_led: {}".format(self.siren_led))
        print("self.moveconv_motorin1: {}".format(self.moveconv_motorin1))
        print("self.moveconv_motorin2: {}".format(self.moveconv_motorin2))
        print("self.moveconv_motorpwm: {}".format(self.moveconv_motorpwm))
        print("self.destconv_motorin1: {}".format(self.destconv_motorin1))
        print("self.destconv_motorin2: {}".format(self.destconv_motorin2))
        print("self.destconv_motorpwm: {}".format(self.destconv_motorpwm))
        print("self.remove_stopperservo: {}".format(self.remove_stopperservo))
        print("self.escape_relayswitch: {}".format(self.escape_relayswitch))
        print("self.explode_led: {}".format(self.explode_led))
        print("self.explode_temp1: {}".format(self.explode_temp1))
        print("self.explode_temp2: {}".format(self.explode_temp2))
        print("self.first_button: {}".format(self.first_button))
        print("self.second_button: {}".format(self.second_button))
        print("self.shutdown_button: {}".format(self.shutdown_button))
        print("self.boot_led: {}".format(self.boot_led))


if __name__ == "__main__":
    rpg = ReadPinFig()
    rpg.show()
