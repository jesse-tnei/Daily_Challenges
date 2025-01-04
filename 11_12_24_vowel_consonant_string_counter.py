def vowel_consonant_string_counter():
    """
    Loops through the sentence provided by the user on the terminal to count the number of vowel and consonant
    characters
    :param
        sentence: str
            Program prompts the user to provide the sentence via the terminal
    :return
        num_vowels: int
            the number of vowels counted in the sentence
        num-consonant: int
            the number of consonants in the sentence
    :raises
        prints warning message if user does not enter sentence then asks user to enter sentence again
        prints warning message if the whole of user sentence is made up of only integer values

        Note: The user is allowed to enter a sentence that contains a mixture of integers and characters
    """

    # Initialise a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

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

        # initialise vowel counter
        vowel_count = 0

        # Initialise a list of all the lower alphabets stripped of the digits and whitespace
        stripped_lower_letters = []

        # Loop through the sentence with three goals
        # One, ignore the whitespace and digits and convert all letters to lower case
        # Two, create a new list of elements containing only the letters
        # Three, increment the counter for the vowels

        for i in sentence:
            if i.isalpha():

                # append all the alphabetical letters into the new list
                stripped_lower_letters.append(i)

                # then loop through the vowels list
                for j in vowels:
                    # if the alphabet in sentence is a vowel, increment vowel counter by 1
                    # note that we turn it into lower case first before comparison

                    if i.lower() == j:
                        vowel_count += 1

        # Check the new list of only letters to subtract the number of vowels such that we are left with only
        # consonants
        consonant_count = len(stripped_lower_letters) - vowel_count

        return vowel_count, consonant_count


vowels_counted, consonants_counted = vowel_consonant_string_counter()

print(f'Vowel count: {vowels_counted}')
print(f'Consonant count: {consonants_counted}')
