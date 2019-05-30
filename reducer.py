#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:52:05 2019

@author: Bryan
"""

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    # print(line)
    # word, count = line.split('\t', 1)
    word, count = line.split(' ')
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(current_word, current_count)
        current_count = count
        current_word = word
if current_word == word:
    print(current_word, current_count)
    
    
    
