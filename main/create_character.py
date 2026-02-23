"""code for creating your character"""

import functions

def choose_name():
    """define the character's name"""

    print("enter your name")
    name = input()

    if len(name) == 0:
        functions.text("you should probably enter a name that exists")
        name = choose_name()
        return name
    else:
        return name

def choose_species():
    """define the character's species"""

    print("ok gang")
    print("there's a lot of different species you can choose now")

    print()

    species = input()

    if len(species) == 0:
        functions.text("you should probably enter a name that exists")
        species = choose_species()
        return species
    else:
        return species

    return species