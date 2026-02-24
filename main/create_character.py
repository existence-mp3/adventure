"""code for creating your character"""

import functions
import story

def choose_name():
    """define the character's name"""

    print("enter your name")
    name = input()

    if len(name) == 0:
        functions.text("you should probably enter a name that exists")
        name = choose_name()
        story.character.name = name
        return name
    else:
        story.character.name = name
        return name

def choose_species():
    """define the character's species"""

    functions.text("ok gang")
    functions.text("there's a lot of different species you can choose now")
    print("enter your species")

    print()

    species = input()

    if len(species) == 0:
        functions.text("you should probably enter a species that exists")
        species = choose_species()
        story.character.species = species
        return species
    else:
        story.character.species = species
        return species

def choose_calling():
    """define the character's class"""

    functions.text("time for your calling!")
    functions.text("this is a wild one")
    functions.text("your calling is gonna determine what you do in battles")
    print("enter your calling")

    print()

    calling = input()

    if len(calling) == 0:
        functions.text("you should probably enter a calling that exists")
        calling = choose_calling()
        story.character.calling = calling
        return calling
    else:
        story.character.calling = calling
        return calling
