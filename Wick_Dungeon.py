# Gavin & Isaac
# 10/31/19
# Hartwick Dungeon

import random


def roll_dice():
    roll = random.randint(2, 12)
    return roll


def create():
    print("Welcome to the Hartwick Dungeon!")
    print("Would you like to play as a Warrior or a Sorcerer?")
    print("Be careful which you choose, both have different advantages!")
    print("Warriors stand a greater chance of living against goblins...")
    print("Though Sorcerers stand a greater chance of living against withces...")
    print("Please type '1' for Warrior, or '2' for Sorcerer.")
    character = int(input("> "))
    if character == 1:
        print("You have selected Warrior.")
    elif character == 2:
        print("You have selected Sorcerer.")
    else:
        print("That is an invalid selection. Please enter '1' or '2'")
        character = int(input())
        if character == 1:
            print("You have selected Warrior!")
        elif character == 2:
            print("You have selected Sorcerer!")



def play_game():






