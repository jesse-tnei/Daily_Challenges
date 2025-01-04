import unicodedata

minimum_username_length = 5
maximum_username_length = 15


def username_validity():
    """
    Loops through the username string provided by the user to check its validity based on these three factors:
            1. Username length is between 5 and 15 characters
            2. Username contains only alphanumeric characters - no punctuations
            3. Username starts with a letter
    Note: to function uses the unicodedata library to cater for non-english usernames

    :param
        username: str
            the user is prompted to provide their username via the terminal

    :return:
        str: 'Valid username' if all the conditions are met
        str: 'Invalid username, only letters and numbers allowed' if special characters and whitespaces are found
        str: 'Invalid username, length below 5' if username length shorter than 5
        str: 'Invalid username, length above 15' if username length is longer than 15
        str: 'Invalid username, first character not a letter' if the first character is not a letter

    :warning
        str: 'Username not entered' if the user runs the program without providing their username of choice

    ## KEY LEARNING: The continue function, when implemented with while, takes the program back to the start
    """
    welcome_message = ('Welcome to the username validator program. Enter your username as instructed below\n'
                       'Type q and press Enter to exit the program.\n')
    username_prompt = ('Type username here then press Enter to check its validity.\n'
                       'Note that your username must:\n'
                       '    1. Be between 5 and 15 characters\n'
                       '    2. Must contain only letters and numbers - no special characters\n'
                       '    3. Must start with a letter\n'
                       'Username: ')
    print(welcome_message)
    while True:

        # Obtain username first
        username = unicodedata.normalize('NFKD', input(username_prompt).strip())

        # Check exit condition
        if username.lower() == 'q':
            print('Program closing. Thank you for using our services')
            break

        # Then check if user actually provided a username if they are not exiting
        if not username:
            print('No username detected. Please try again')

            if username == 'x':
                continue

        # If user provided username, validate the length. These two can be done within the same code 'room'
        if len(username) < minimum_username_length:
            print(f'Invalid username. Length must be at least {minimum_username_length} characters')
            continue
        elif len(username)> maximum_username_length:
            print(f'Invalid username. Name must be at most {maximum_username_length} characters')
            continue

        # Now validate if first character is alphanumeric
        if not username[0].isalpha():
            print('Invalid username. First character in username must be a letter')
            continue

        # Finally, validate the alphanumeric character
        if not username.isalnum():
            print('Invalid username. Only letters and numbers allowed')
            continue

        # Finally, if all the passes have been met
        print('Valid username')
        break


username_validity()
