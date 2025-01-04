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
    print('Welcome to the sentence reversal tool')
    while True:

        # Get sentence and remove any trailing whitespace surrounding it
        sentence = input('Enter sentence to be reversed here. Type q and press Enter to quit: ').strip()

        # Sentence list must be greater than 1 character for reversal. If not, user enters new sentence.
        if len(sentence) <= 1:
            if sentence.lower() == 'q':
                print('Program closing, click run to restart')
                break
            else:
                print('Sentence too short to be reversed, please enter sentence with more than one character')
                continue

        # Use the in-built reversed function to generate a new sentence
        return ''.join(char for char in reversed(sentence))


print(f'Reversed sentence: {reverse_string()}')
