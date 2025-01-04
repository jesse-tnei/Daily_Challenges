def vowel_counter():
    """
    Loops through the sentence string provided by user on the terminal and returns the number of vowels present in that
    string

    :param
        sentence str
            Program prompts the user to provide the sentence as a string input on the terminal
            Note: This is not taken as the program's direct input, but as a parameter generated within the program itself

    :return
        vowel_count int
            The number of vowel characters present in sentence string

    raises:
        prints warning message if no input string has been provided
    """
    print('Welcome to the vowel counter')
    while True:

        # Begin with getting user input and remove any trailing whitespace
        sentence = input('Type sentence here then press Enter. Type q then Enter to exit program: ').strip()

        # First check if the user provided any kind of input. If not, prompt them to provide that input
        if not sentence:
            print('No input detected. Please try again')
            continue

        # If input was provided, check if that was to instruct the program to close
        if sentence.lower() == 'q':
            print('Program closing, thank you for using our services')
            break

        # If input was provided and was an actual string, set up vowel parameters for system to refer to
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Then instantiate the generator that checks for vowels, produces a 1 each time it finds one, and summates
        # the overall vowel count
        vowel_count = sum(1 for i in sentence.lower() if i in vowels)

        # Then we print it out
        print(f'Vowel count is:{vowel_count}')

    return vowel_count


vowel_counter()
