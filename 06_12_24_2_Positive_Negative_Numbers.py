def number_check():
    """ Iteratively checks to see if the number given by the user is positive or negative

    Parameters
    __________
    number: int
        The number to be checked

    Returns
    _______
    String message - 'Positive' if number is zero or positive, 'Negative' if number is negative

    Raises
    ______

    """

    while True:
        number_to_check = input('Enter number as a digit here. For example, 9: ')

        # Note that the l_strip removes the leading element in the given user input
        # This is another form of string manipulation that we should probably remember
        if not number_to_check.lstrip('-').isdigit():
            raise ValueError('Please enter number as a digit and not a string')

        number_to_check = int(number_to_check.strip())

        if number_to_check >= 0:
            print('Positive')
        else:
            print('Negative')


number_check()
