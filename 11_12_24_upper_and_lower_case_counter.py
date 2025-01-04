def upper_and_lower_case_counter():
    """
    Loops through a sentence provided by user in the terminal and returns the number of characters that are in upper
    and lower case format
    :param
        sentence: str
            sentence is a string provided by the user following the input prompt
    :return:
        num_upper: int
            number of uppercase letters
        num_lower: int
            number of lower case letters
    :raises
        prints out a warning message if the user enters an empty string or integer pure integer numbers
        prints out a warning message if the user does not enter a sentence on the terminal
        In both instances, offers user the chance to re-enter a new sentence as input
    """
    print('Welcome to the upper/ lowercase character counter')
    while True:
        sentence = input('Enter sentence here: ').strip()

        if not sentence:
            print('No sentence input detected, please type a sentence at the blinking cursor on the terminal'
                  ' and press Enter to try again')
            continue
        # Note, this returns true only if all the characters are digits and false if it's a mix
        # We use this to avoid having to loop through all the characters one-by-one
        if sentence.isdigit():
            print('You entered a number instead of a string-version sentence. Please check input and try again')
            continue

        num_upper = 0
        num_lower = 0
        for i in sentence:
            # Note that this explicitly filters out the alphabetical characters and ignores the spaces and digits
            if i.isalpha():
                if i.isupper():
                    num_upper += 1
                if i.islower():
                    num_lower += 1
        return num_upper, num_lower


upper, lower = upper_and_lower_case_counter()
print(f'Number of upper case characters: {upper}. Number of lower case characters: {lower}')
