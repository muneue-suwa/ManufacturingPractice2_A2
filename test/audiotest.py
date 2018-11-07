#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:59:31 2018

@author: crantu
"""

import pygame.mixer
from time import sleep
import subprocess

# amixer -M
cmd = ["amixer", "-M"]
proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("$ amixer -M")
print(proc.stdout.decode("utf8"))

pygame.mixer.init()
pygame.mixer.music.load("../../MP2_A2_audiofiles/AudioFiles/trumpet1.mp3")
pygame.mixer.music.play(-1)
sleep(60)
pygame.mixer.music.stop()
