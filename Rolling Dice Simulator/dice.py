import random

roll_dice = input('Do you want to roll the dice: ')
yes = "Y"
no = "N"


def roll():
    if(roll_dice == yes):
        print('Rolled: ', random.randrange(1, 6),
              'and', random.randrange(1, 6))
    elif(roll_dice == no):
        print('Game dismissed')


roll()


def again():
    var = 10
    while(var == 10):
        roll_again = input('Do you want to roll again: ')
        if(roll_again == yes):
            roll()
        elif(roll_again == no):
            print('Game dismissed')
            break


again()
