#! /usr/bin/python3
import os
from time import sleep

internal_count = 0
sec = 0
min = 0

while min != 25:
    sleep(1)
    sec += 1 
    if sec % 60 == 0:
       min += 1
       sec = 0
    timed = f'{min}:{sec}'
    os.system('clear')
    print(timed)

print("You have finnished")
