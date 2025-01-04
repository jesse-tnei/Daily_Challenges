import random
import numpy


def dice_roll():
    """
    Generates a random dice number for a range defined by the user as the number of dice faces

    :param
        dice_faces: str
            Provided as string by the user in the terminal but should be a digit which is then
            converted to an integer

    :return: int
    A random integer value between 1 and the integer input provided by the user
    :raises
    terminal warning print if the user provides the number as a word instead of a digit
    """
    print('Welcome to the dice roll simulator')
    while True:
        dice_faces = input('Enter the number of dice faces as a digit. Type Q and press Enter to exit program: ')

        if not dice_faces.isdigit():
            if dice_faces.strip().lower() == 'q':
                print('Program closing')
                break
            else:
                print('Please enter the number as a digit instead of string')
                continue

        if int(dice_faces)<=1:
            print('Dice cannot have 0,1  or negative number of faces, please try again')
            continue

        random_number = random.randint(1, int(dice_faces))
        print(f'You rolled a: {random_number}')
        continue
    return random_number


dice_roll()
