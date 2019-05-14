#! /usr/bin/python3

from time import sleep
from colorama import Fore, Back, Style
from pydub import AudioSegment
from pydub.playback import play
import pydub
import os


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "./tibetan-bowl-right-hit.wav")


def run(tmin = 0,sec = 0, filename=filename):
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
        if tmin < 24:
          print(Fore.GREEN, Back.BLACK + timed)
        else:
          print(Fore.BLACK, Back.RED + timed)

    print(Style.RESET_ALL)
    os.system("clear")
    print("You have finished")

    try:
        sound = AudioSegment.from_file(filename, format="wav")
        play(sound)
    except:
        print('Unable to play sound',err)


if __name__ == ('__main__'):
    run(0,0)
