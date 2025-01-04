import string


def word_length_counter():
    """
    Loops through the words forming the sentence string input and returns the longest word with its associated
    character count
    :param sentence: str
        Provided by the user as part of the input
    :return:
        printed statement 1: 'The number of words in the sentence is: {len(list_of_words_in_sentence)}'
        printed statement 2: "The longest word in the sentence, '{longest_word}' has
        {len(longest_word)} characters"
    """

    print('Welcome to the word counter')

    while True:
        sentence = input('Enter type sentence and press Enter to continue: ')

        if not sentence:
            print('No words in sentence, please add a sentence with words and try again')
            continue
        list_of_words_in_sentence = [word.strip(string.punctuation) for word in sentence.split()]

        longest_word_index = 0

        for current_position, current_word in enumerate(list_of_words_in_sentence):
            if len(current_word) > len(list_of_words_in_sentence[longest_word_index]):
                longest_word_index = current_position

        longest_word = list_of_words_in_sentence[longest_word_index]

        print(f'The number of words in the sentence is: {len(list_of_words_in_sentence)}')
        print(f"The longest word in the sentence, '{longest_word}' has "
              f"{len(longest_word)} characters")


word_length_counter()
