"""basic functions used all over the place"""

import sys
import create_character
import story

def pause():
    """pauses text until the enter key is pressed"""
    command = input()
    sys.stdout.write('\033[A\033[K')
    sys.stdout.flush()
    if command == "rename":
        create_character.choose_name()
        text(f"you are now named {story.character.name}")

def text(message):
    """prints a message and then requires enter key to continue"""
    print(message)
    pause()
