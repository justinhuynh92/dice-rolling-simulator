#import random
import random

#define a function to roll the dice
def roll_dice():

    roll = input("Roll the dice? (Yes/No): ")

    #create while loop that makes input lowercase
    while roll.lower() == "Yes".lower():
        #assign random integer between 2 inputted numbers
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        #print a statement that has a dictionary formatted for dice1 and dice2
        print("dice rolled: {} and {}".format(dice1, dice2))
#create a dictionary that will have the drwaings of the dice
