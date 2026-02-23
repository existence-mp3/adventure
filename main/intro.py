"""main code for adventure"""

import functions
import create_character

def intro():
    """print commands that trigger when you start the game"""

    print()

    functions.text("welcome to adventure®")
    functions.text("this will be the most pointless experience of your life")
    functions.text("yes you read that right we trademarked the word adventure")
    functions.text("we will hit you with a ten billion dollar defamation lawsuit if you say it")

    print()

    name = create_character.choose_name()

    print()

    functions.text(f"{name}, welcome to the town of digit")
    functions.text("there's a lot of people here who are a little bit obsessed with digits")

    print()

    functions.text("now we have to lock in on what you look like")
    functions.text("that means it's time to choose your species")

    print()

    species = create_character.choose_species() # work on all the different species options

    print()

    functions.text(f"stupendous. you are officially a {species}")

intro()
