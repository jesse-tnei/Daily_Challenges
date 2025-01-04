# Helper function to confirm if the float is a valid number
def is_valid_float(number):
    return number.replace('-', '', 1).replace('.', '', 1).isdigit() and number.count('-') <= 1 and number.count(
        '.') <= 1


def sign_check(allow_float=False):
    """
    Checks if user-provided number is positive or negative. Supports both integer and float inputs
    :param
        allow_float: bool
        If True the function will validate both float and integer inputs
        If False, the function will validate only integer inputs

    :return:
    This function does not return a value. Instead it prints whether the input is:
        1. A positive integer
        2. A negative integer
        3. A positive float
        4. A negative float

    :raises
    This function prints an error message when:
        1. The input contains multiple negative signs or decimal points
        2. The input contains other non-numeric characters
    """

    # Print out the welcome message
    print('Welcome to the positive-negative check')

    # Set up the infinite loop for repetitive function performance
    while True:
        # Capture user input
        number = input('Enter number here. Type q and press Enter to exit: ').strip()

        # Set up the exit condition immediately
        if number.lower() == 'q':
            print('Program closing, thank you for using our services')
            break

        # Validate input for integers

        # check for positive numbers
        if number.isdigit():
            print(f'{number} is a positive integer')
            continue

        # check for negative numbers
        if number.startswith('-') and number[1:].isdigit():
            print(f'{number} is a negative integer')
            continue

        # Validate input for floats if allowed
        if allow_float and number.count('.') == 1 and is_valid_float(number):
            if number[0] == '-':
                print(f'{number} is a negative float')
            else:
                print(f'{number} is a positive float')
            continue

        # Handle invalid input
        print('Invalid input. Please ensure number is properly formatted with digits, a singe decimal point (if '
              'allowed and at most, one leading negative sign')


sign_check(True)
