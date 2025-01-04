def reverse_string():
    """
    Loops through a user-provided sentence from the terminal and returns its reversed version
    :param
        sentence:str
            user provides the sentence to be reversed as prompted on the terminal
    :return:
        new_sentence: str
            the new mirrored/ reversed sentence
    :raises
        A prompt to warn user if sentence is less than one character as reversal cannot be performed. Offers user
        opportunity to provide a new sentence that meets the pre-requisites
    """
    while True:

        # Get sentence
        sentence = input('Enter sentence to be reversed here: ').strip()

        # Convert sentence to list
        sentence_as_list = [i for i in sentence]

        # Sentence list must be greater than 1 character for reversal. If not, user enters new sentence.
        if len(sentence_as_list) <= 1:
            print('Sentence too short to be reversed, please enter sentence with more than one character')
            continue

        # Initialise last sentence list index to be used for reversal
        reverse_index = len(sentence) - 1

        # Loop through to perform the reversal
        for char_position, char in enumerate(sentence):
            sentence_as_list[reverse_index] = char
            reverse_index -= 1

        # Join the reversed list with no separation and return as the new sentence
        return ''.join(sentence_as_list)


print(f'Reversed sentence: {reverse_string()}')
