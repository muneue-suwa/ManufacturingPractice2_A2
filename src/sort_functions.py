#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 08:29:42 2018

@author: crantu
"""


class SortFunctions:
    def __init__(self, sorted_func_name_list, func_dict):
        self.func = []
        for item in sorted_func_name_list:
            self.func.append(func_dict[item])
