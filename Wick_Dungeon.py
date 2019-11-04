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
    play_game(character)


def play_game(character):
    print("You have entered your first dungeon!")
    print("You are faced with a Goblin!")
    print("If you are a Warrior, you must roll a number above 6 to survive..")
    print("But if you are a Sorcerer, you must roll a number above 7 to survive..")
    print("If your roll is less than the numbers required, you start all over!")
    roll_1 = roll_dice()
    print(f"You rolled a {roll_1}.")
    if character == 1 and roll_1 > 6:
        print("You have survived! On to your next challenge!")
    elif character == 1 and roll_1 < 6:
        print("You have died! Would you like to try again?")
        print("Please enter 'y' or 'n'.")
        answer = input("> ")
        if answer == "y":
            create()
        elif answer == "n":
            print("Thanks for playing!")
    if character == 2 and roll_1 > 7:
        print("You have survived! On to your next challenge!")
    elif character == 2 and roll_1 < 7:
        print("You have died! Would you like to try again?")
        print("Please enter 'y' or 'n'.")
        answer = input("> ")
        if answer == "y":
            create()
        elif answer == "n":
            print("Thanks for playing!")





create()
