#! /usr/bin/python3

import os
from time import sleep
import pydub

def run(tmin = 0,sec = 0):
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
    from pydub import AudioSegment
    from pydub.playback import play

    sound = AudioSegment.from_file("tibetan-bowl-right-hit.wav", format="wav")
    play(sound)
if __name__ == ('__main__'):
    run(24,50)
