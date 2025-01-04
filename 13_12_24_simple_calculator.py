operations = ['addition', 'subtraction', 'multiplication', 'division']


def operation_capture():
    """
    Captures the type of mathematical operation that the user wishes to perform and stores it as a number associated to
    a list. Additionally, offers the opportunity for user to terminate program by typing 'q' on the terminal

    :param
        No explicit parameter taken in. The function, instead, prints out a list of all the possible operations that
        the calculator can perform with each operation having an associated number between 1 and 4.

        The user is then prompted to choose between these operations, entering the number on the terminal as an integer

        The function, however, saves this number as a string and returns it as the operation_type variable


    :return:
        operation_type str
            string type ranging between '1' and '4'.

    :raises
        prints out a warning message if no operation was detected as the terminal input
        prints out a warning message if the operation entered by the user on the terminal is of a non-integer type. Only
        time this message is not printed out is when user enters 'q' which, instead, terminates the program
        prints out operation if the integer input entered by user on terminal is beyond the range
    """
    while True:

        # Present user with operations that the calculator can perform
        for operation_index, operation in enumerate(operations):
            print(operation_index + 1, operation)

        operation_type = input('Select the operation that you wish to perform\n'
                               'by typing its associated number from the above list\n'
                               'and then press Enter to choose that operation.\n'
                               'Type q and press Enter to exit program: ').strip()

        # If user has not selected operation, inform them and go back to beginning of the while loop
        if not operation_type:
            print('No operation selected. Please try again')
            continue

        # Check if user typed q to close program
        if operation_type.lower() == 'q':
            print('Exiting program. Thank you for using our services')
            break

        # Check if user selected a non-integer option
        if not operation_type.isdigit():
            print('Non-integer input detected, please select an integer option from the above operation list')
            continue

        # Check if user selected an integer option but not within the list
        if int(operation_type) > len(operations):
            print('The selected operation is not within the list of choice, please check input and try again')
            continue
        return operation_type


def integer_capture():
    """
    Captures the integer that the user wishes to use to perform mathematical operations. Additionally,
    offers the opportunity for user to terminate program by typing 'q' on the terminal

    :param
        No explicit parameter taken in. The function, instead, prompts the user to enter the number as a digit


    :return:
        int_ int
            integer variable int_ to be used later in the mathematical operation

    :raises
        prints out a warning message if no operation was detected as the terminal input
        prints out a warning message if the operation entered by the user on the terminal is of a non-integer type. Only
        time this message is not printed out is when user enters 'q' which, instead, terminates the program
        prints out operation if the integer input entered by user on terminal is beyond the range
    """
    while True:
        # Prompt to get the user's input
        int_ = input(
            'Type number and press Enter to provide number. Type q and press Enter to exit program: ')

        # Check to see if user provided input
        if not int_:
            print('Input not detected. Try type the number again')
            continue

        # Check if user typed q to close program
        if int_.lower() == 'q':
            print('Exiting program. Thank you for using our services')
            break

        # Check to see if input is a digit number
        if not int_.isdigit():
            print('Non-integer detected for input. Please try typing and integer input again')
            continue

        return int(int_)


def simple_calc():
    """
    Uses the two integer numbers and the mathematical operation type as specified by the user to perform the mathematical
    operation and return the results

    :param
        No explicit parameter needed from the user. Instead, the function calls two other functions - operation_capture
        to get the type of operation that the user wishes to perform - and integer_capture to prompt the user to enter
        the two digits upon which the mathematical operation is to be implemented
    :return:
        None
        Instead, prints out a statement to inform the user of the two integers entered, the operation performed and
        the result gotten out of that operation

    :raises

    """

    # Welcome message
    print('Welcome to your simple calculator')

    while True:

        # CAPTURING FIRST USER INPUT
        integer_one = integer_capture()
        print('First integer: ', integer_one)

        if integer_one != 0:
            if not integer_one:
                break

        # CAPTURING OPERATION TYPE USING THE OPERATION CAPTURE FUNCTION
        operation_type = operation_capture()
        print('Chosen operation type:', operations[int(operation_type) - 1])

        if not operation_type:
            break

        # CAPTURING SECOND USER INPUT
        integer_two = integer_capture()
        print('Second integer: ', integer_two)

        if integer_two != 0:
            if not integer_two:
                break

        # PERFORMING THE CALCULATIONS
        # Addition
        if operation_type == '1':
            print(f'Sum of {integer_one} and {integer_two} is {integer_one + integer_two}')

        # Subtraction
        if operation_type == '2':
            print(f'Difference between {integer_one} and {integer_two} is {integer_one - integer_two}')

        # Multiplication
        if operation_type == '3':
            print(f'Product of {integer_one} and {integer_two} is {integer_one * integer_two}')

        if operation_type == '4':
            if integer_two == 0:
                print('Division operation not possible as denominator is zero. Please try again')
                continue
            else:
                print(f'Quotient of {integer_one} and {integer_two} is {integer_one / integer_two}')


simple_calc()
