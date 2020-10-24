import os
import itertools
import sys
import time


red = '\
        -----\n\
        | * |\n\
        | . |\n\
        | . |\n\
        -----\n\
        '
yellow = '\
        -----\n\
        | . |\n\
        | * |\n\
        | . |\n\
        -----\n\
        '
green = '\
        -----\n\
        | . |\n\
        | . |\n\
        | * |\n\
        -----\n\
        '

colours = itertools.cycle([red, green, yellow])

os.system('clear')
while True:
    sys.stdout.write('\r' + next(colours))
    sys.stdout.flush()
    time.sleep(1)
    os.system('clear')
