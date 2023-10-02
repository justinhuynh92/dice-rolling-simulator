#import random
import random

#define a function to roll the dice
def roll_dice():

    #dice drawing code
    dice_drawing = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }

    roll = input("Roll the dice? (Yes/No): ")

    #create while loop that makes input lowercase
    while roll.lower() == "Yes".lower():
        #assign random integer between 2 inputted numbers
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        #print a statement that has a dictionary formatted for dice1 and dice2
        print("dice rolled: {} and {}".format(dice1, dice2))
        #print dice drawing instead of just integers
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        #ask user if they want to roll again
        roll = input("Roll again? (Yes/No): ")

#run function
roll_dice()
