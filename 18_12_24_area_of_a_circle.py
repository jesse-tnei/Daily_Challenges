import math


def is_valid_float(number):
    return number.replace('.', '', 1).isdigit() and number.count(
        '.') <= 1


def circle_area():
    """
    Prompts the user to provide the radius of a circle as an integer on the terminal and returns the area of the circle
    :param
        The function takes no explicit input parameters. Instead, it prompts user to enter circle radius on the terminal
    :return:
        None. Keeps running until user exits
        Note, function closes when user types q and presses Enter
    :raises
        Prints warning if and restarts operations if:
            1. No input is detected on the terminal
            2. User enters a negative or non-integer value for the radius

    Important link for code modularisation: https://www.youtube.com/watch?v=P7wlBTLYyrg&ab_channel=TheCodeGuy
    """

    # display welcome message
    print('Welcome to the circle area calculator')

    # set up while loop for repetitive function operation
    while True:

        # capture user input for the circle radius
        radius = input('Enter radius of the circle in cm and as an integer. Type q and press enter to exit: ').strip()

        # check if user entered an input, if not, prompt user to enter input
        if not radius:
            print('No input detected. Please try again')
            continue

        # close program is user wishes to exit
        if radius.lower() == 'q':
            print('Program closing, thank you for using our services')
            return None

        # confirm if input is digit or float
        if radius.isdigit() or is_valid_float(radius):
            radius = float(radius)  # Convert to float for calculation
            area = math.pi * radius * radius
            print(f'The area of a circle with radius {radius:.2f} cm is {area:.2f} square cm.')
        else:
            print('Invalid input. Please not that the radius has to be a non-negative integer or float value')


circle_area()
