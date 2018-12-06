#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 23:08:04 2018

@author: crantu
"""

from os import path


def make_crontab():
    mp2_crontab = (r"@reboot bash "
                   r"{home_dir}/Git/ManufacturingPractice2_A2/start.sh"
                   r" >> {home_dir}/Git/ManufacturingPractice2_A2/log/"
                   r"mp2_cron_$(date +\%Y\%m\%d_\%H\%M\%S).log 2>&1")
    shutdown_button_crontab =\
        (r"@reboot python3 "
         r"{home_dir}/Git/ManufacturingPractice2_A2/"
         r"shutdown_button/shutdown_button.py"
         r" >> {home_dir}/Git/ManufacturingPractice2_A2/log/"
         r"shutdown_button_$(date +\%Y\%m\%d_\%H\%M\%S).log 2>&1")
    dir_name = path.dirname(path.abspath(__file__))

    mp2_crontab = mp2_crontab.format(home_dir=path.expanduser("~"))
    shutdown_button_crontab =\
        shutdown_button_crontab.format(home_dir=path.expanduser("~"))

    with open(path.join(dir_name, "mp2.crontab"), "w") as f1:
        f1.write(mp2_crontab)
        f1.write("\n")
    with open(path.join(dir_name, "shutdown_button.crontab"), "w") as f2:
        f2.write(shutdown_button_crontab)
        f2.write("\n")
    print(mp2_crontab)
    print(shutdown_button_crontab)


if __name__ == "__main__":
    make_crontab()
