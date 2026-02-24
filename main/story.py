"""main code for adventure"""

import functions
import create_character
import character

character = character.Character()

def intro():
    """print commands that trigger when you start the game"""

    print()

    functions.text("welcome to adventure®")
    functions.text("this will be the most pointless experience of your life")
    functions.text("yes you read that right we trademarked the word adventure")
    functions.text("we will hit you with a ten billion dollar defamation lawsuit if you say it")

    print()

    create_character.choose_name()

    print()

    functions.text("okey dokey")
    functions.text("you can change your name by typing rename")
    functions.text(f"{character.name}, welcome to the town of digit")
    functions.text("there's a lot of people here who are a little bit obsessed with digits")

    print()

    functions.text("now we have to lock in on what you look like")
    functions.text("that means it's time to choose your species")

    print()

    create_character.choose_species() # work on all the different species options

    print()

    functions.text(f"stupendous. you are officially a {character.species}")

    print()

    functions.text("anyway, back to the story")
    functions.text("you are visiting the town of digit")
    functions.text("you have rented a room in inn 6")
    functions.text("at first you were gonna go with inn 2")
    functions.text("but you decided the rooms were better in inn 6")

    print()

    functions.text("today, you decided to go for a walk")
    functions.text("but then some feral hogs started attacking the town")
    functions.text("all the people were like 'arr narr!'")
    functions.text("but you're kinda locked in")
    functions.text("you know how to fight...")
    functions.text("vaguely...")

    print()

    functions.text("so...")
    functions.text("guess what that means!")
    create_character.choose_calling() # work on all the different calling options
