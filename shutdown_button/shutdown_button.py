#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:47:29 2018

@author: wincrantu
"""

from gpiozero import Button, LED
from signal import pause
import shlex
import subprocess


class ShutdownButton:
    def __init__(self):
        self.boot_led = LED(4)
        self.shutdown_button = Button(2)

    def say_hello(self):
        print("Hello!")
        self.boot_led.off()

    def pyshutdown(self):
        self.boot_led.off()
        command_line = "sudo shutdown -h now"
        args = shlex.split(command_line)
        print(command_line)
        return subprocess.Popen(args)

    def shutdown_with_button(self):
        self.boot_led.on()
        self.shutdown_button.when_pressed = self.pyshutdown
        pause()


if __name__ == "__main__":
    sb = ShutdownButton()
    sb.shutdown_with_button()
