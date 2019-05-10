#! /usr/bin/python3
import os
from time import sleep


def run(sec = 0, tmin = 0):
    sec = sec
    tmin = tmin

    while tmin != 25:
        sleep(1)
        sec += 1 
        if sec % 60 == 0:
           tmin += 1
           sec = 0
        timed = f'{tmin}:{sec}'
        os.system('clear')
        print(timed)

    print("You have finished")


if __name__ == ('__main__'):
    run(50,24)
