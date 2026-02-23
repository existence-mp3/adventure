"""basic functions used all over the place"""

import sys

def pause():
    """pauses text until the enter key is pressed"""
    input()
    sys.stdout.write('\033[A\033[K')
    sys.stdout.flush()

def text(message):
    """prints a message and then requires a keystroke to continue"""
    print(message)
    pause()
