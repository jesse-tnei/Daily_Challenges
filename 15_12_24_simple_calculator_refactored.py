operations = ['addition', 'subtraction', 'multiplication', 'division']


def validate_input(prompt, allow_float=False):
    """
    Helper function to validate user input, allowing for integers, floats and negative numbers

    :param
        prompt: str
            The message to be displayed to the user before they provide their input
    :param
        allow_float: bool, optional
            a flag to be adjusted by the user if they wish to provide float numbers. By default, set to accept integer
            numbers only
    :return:
        int or float. The validated user input as an integer or float
        None: if the user types q which prompts the closure of the program

    :raises
        No explicit exceptions raised. Prints error message for invalid input i.e., if input is out of range
    """

    while True:
        # capture user input and remove any trailing whitespaces
        user_input = input(prompt).strip()

        # Check if user wishes to quit the program
        if user_input.lower() == 'q':
            print('Exiting program, thank you for using our services')
            return None

        # Check for valid float or integer

        # Check for float
        if allow_float:
            if (user_input.replace('-', '', 1).replace('.', '', 1).isdigit() and
                    user_input.count('-') <= 1 and user_input.count('.') <= 1 and user_input[0] in '-0123456789'):
                return float(user_input)
        # Check for integer number
        else:
            if (user_input.replace('-', '', 1).isdigit() and user_input.count('-') <= 1
                    and user_input[0] in '-0123456789'):
                return int(user_input)

        # If none of the conditions are met, print message and restart loop
        print("Invalid input. Please enter a number or type 'q' and press Enter to quit program: ")


def operation_capture():
    """Captures the mathematical operation to be performed"""

    # Print operations available for user to choose from - printing with their associated numbers i.e., index + 1
    print('Available operations')
    # the 1 in enumerate instructs the counting to start from 1 instead of 0
    for operation_index, operation in enumerate(operations, 1):
        print(operation_index, operation)

    while True:
        choice = validate_input("Select operation by typing number associated with it as integer and pressing Enter"
                                "Type 'q' and press Enter to exit program: ")

        # Choice is None is where the user wants to quit, remember we said return None
        if choice is None:
            return None

        # Check to see if the choice that user is an integer first and then if it's within the 1 - 4 range
        if isinstance(choice, int) and 1<= choice <= len(operations):
            # we convert it back to string since our calculation function considers string scenarios
            return str(choice)

        # If the choice was not None, was a float or was outside the range of 1 - 4
        print('Invalid selection, please choose a valid operation')


operation_capture()