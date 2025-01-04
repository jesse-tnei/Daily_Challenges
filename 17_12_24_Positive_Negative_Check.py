def sign_check(allow_float=False):
    """
    Checks user integer input to confirm is the number is positive or negative

    :param allow_float: bool allows user
    to specify if the number they wish to check is an integer or a float number Setting it to false would result in
    the function not printing anything out as it will not perform the float check

    Also, once program is running, it prompts user to enter the number as digits on the terminal
    with decimal points and negative numbers


    :return:
        prints statement to inform if the number is positive integer, positive float, negative integer, negative float

    :raise
        prints warning if the negative sign appears at a non-leading position for both the float and the integer numbers
    """

    # Welcome message
    print('Welcome to the positive negative check')

    # Repetitive program cycle
    while True:

        # Take user input
        number = input('Enter number here. Type q and press Enter to exit the program: ').strip()

        # Confirm if input present, if not, inform user then go back and capture user input
        if not number:
            print('No input detected, please try again')
            continue

        # Check to ensure no non-digit numbers are present
        if not (number.replace('-', '', 1).replace('.', '', 1)).isdigit():
            print('Invalid number. Check your input to confirm only one negative sign, one decimal point and no letters'
                  'or special characters present')
            continue

        # PROGRAM SPLITS INTO TWO - FLOAT AND INTEGER CHECKS
        if number.isdigit():
            print(f'{number} is a positive integer')
        elif (number.replace('-', '', 1)).isdigit() and str(number.count('-')) == '1':
            if number[0] == '-':
                print(f'{number} is a negative integer number')
            else:
                print('Invalid number, negative sign detected at a non-leading position')
                continue

        # Check for float
        if allow_float:
            if (number.replace('.', '', 1)).isdigit() and str(number.count('.')) != '0':
                print(f'{number} is a positive float')
            elif ((number.replace('-', '', 1).replace('.', '', 1)).isdigit() and str(number.count('-')) == '1' and
                  str(number.count('.')) == '1'):
                if number[0] == '-':
                    print(f'{number} is a negative float number')
                else:
                    print(f'{number} is an invalid number. Negative sign detected in a non-leading position')


sign_check(True)
