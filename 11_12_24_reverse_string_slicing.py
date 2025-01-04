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
        if len(sentence) <= 1:
            print('Sentence has less than one character. Provide longer sentence for reversal to be performed')
            return None

        # This is what we are doing here
        # new_sentence = sentence[0: (len(sentence) - 1): - 1]
        # Basically, reassign the characters in sentence from index 0 to last index but move in -1 steps i.e., last (-1)
        # index becomes the first in the new sentence
        # The code we have below as the return is a compact version of this
        return sentence[::-1]


print(reverse_string())
