def vowel_consonant_string_counter():
    """
    Loops through the sentence provided by the user on the terminal to count the number of vowel and consonant
    characters
    :param
        sentence: str
            Program prompts the user to provide the sentence via the terminal. This could contain both letters and digits
            but the program will ignore the digits and spaces such that it counts only the alphabetical elements

    :return
        vowel_count: int
            the number of vowels counted in the sentence
        consonant_count: int
            the number of consonants in the sentence
    :warnings
        prints warning message if user does not enter sentence then asks user to enter sentence again
        prints warning message if the whole of user sentence is made up of only integer values

        Note: The user is allowed to enter a sentence that contains a mixture of integers and characters

        Collections in python - lists, sets and tuples - https://www.youtube.com/watch?v=gOMW_n2-2Mw&ab_channel=BroCode
        Generators compared to lists in python: https://www.youtube.com/watch?v=bD05uGo_sVI&ab_channel=CoreySchafer
    """

    # Initialise a set of vowels
    # Note, we are using sets because generators operate faster on sets compared to lists
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Display welcome message
    print('Welcome to the vowel/ consonant counter')

    while True:

        # Obtain sentence from user and strip it of any whitespace
        sentence = input('Enter sentence for program to check here: ').strip()

        # Check if user added the sentence
        if not sentence:
            print('No sentence input detected. Please type sentence and press enter to continue')
            continue

        # Check if the sentence is only made up of integers
        if sentence.isdigit():
            print('Your sentence is composed of integer values only, please enter a string sentence instead')
            continue

        # We employ the use of generator to filter and produce a 1 every time the vowel conditions are met then summate
        vowel_count = sum(1 for i in sentence if i.isalpha() and i.lower() in vowels)

        # We employ the use of the same generator to count everything then subtract the vowel count such that we are
        # left with consonants only
        consonant_count = sum(1 for i in sentence if i.isalpha()) - vowel_count

        return vowel_count, consonant_count


vowels_counted, consonants_counted = vowel_consonant_string_counter()

print(f'Vowel count: {vowels_counted}')
print(f'Consonant count: {consonants_counted}')
