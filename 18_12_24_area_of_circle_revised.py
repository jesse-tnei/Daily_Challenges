import math


# Helper function to confirm if the float is a valid number
def is_valid_number(number):
    """
    Validates if the input is a properly formatted number (integer or float).

    Parameters:
        number (str): The input string to validate.

    Returns:
        bool: True if the input is a valid number, False otherwise.
    """

    try:
        float(number)
        return True
    except ValueError:
        return False


# Helper function to calculate area of a circle
def area_of_a_circle(radius):
    """
    Computes the area of a circle given its radius.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle calculated using the formula π * r².
    """

    return math.pi * radius ** 2


def area_calculator():
    """
    Prompts the user to provide the radius of a circle as an integer on the terminal and returns the area of the circle

    The function supports non-negative integers and floats as valid inputs

    It repeatedly asks for input until the user chooses to quit

    Behaviour:
     - Takes user input via the terminal
     - Validates user input to ensure it's a non-negative number (integer or float)
     - Calculates the area of the circle using the formula pi* radius squared
     - Prints error message for invalid inputs such as negative values and non-integer/ non-float values
    :param
        None. Inputs are taken from the terminal
    :return:
        None. Output is printed as a message on the console
    :errors
        Prints warning/ error if:
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
        if is_valid_number(radius):
            if float(radius) < 0:
                print('Input radius is negative. Please try again with a positive radius value')
                continue
            else:
                radius = float(radius)  # Convert to float for calculation
                area = area_of_a_circle(radius)
                print(f'The area of a circle with radius {radius:.2f} cm is {area:.2f} square cm.')
        else:
            print('Non-float number detected. Please make sure your input is strictly digits with a single decimal'
                  'point for float radius values')


area_calculator()