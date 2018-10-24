#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:56:58 2018

@author: crantu
"""

import src.fire_and_conveyor
import src.explode_and_escapse


def main():
    fc = src.fire_and_conveyor.FireAndConveyor()
    ee = src.explode_and_escape.ExplodeAndEscape()

    fc.fire_and_conveyor()
    ee.explode_and_escape()
