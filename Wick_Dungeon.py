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
    print()
