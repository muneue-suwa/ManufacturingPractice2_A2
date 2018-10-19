#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:53:39 2018

@author: crantu
"""

import pygame.mixer
import time

# mixerモジュールの初期化
pygame.mixer.init()
# 音楽ファイルの読み込み
pygame.mixer.music.load("AudioFiles/trumpet1.mp3")
# 音楽再生、および再生回数の設定(-1はループ再生)
pygame.mixer.music.play(2)

if input():
    pygame.mixer.music.stop()

# time.sleep(60)
# 再生の終了
pygame.mixer.music.stop()


# Reference: https://qiita.com/Nyanpy/items/cb4ea8dc4dc01fe56918
