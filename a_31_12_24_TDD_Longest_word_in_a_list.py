def length_list(word_string_list):
    # confirm input present
    if not word_string_list:
        raise ValueError('Input is an empty list')

    # confirm input is a list
    if not isinstance(word_string_list, list):
        raise TypeError('Input not a list, please try again')

    # confirm all input elements are string type
    if not all(isinstance(word, str) for word in word_string_list):
        raise ValueError('List contains non-string elements')

    # initialise empty dictionary
    word_len_dict = {}

    # zip the two lists up into a dictionary
    for word in word_string_list:
        word_len = len(word)

        # if first time we are finding word of that length
        if word_len not in word_len_dict:
            # create a list for it in case we come across another word with similar length
            word_len_dict[word_len] = [word]
        else:
            # append new word to original list
            word_len_dict[word_len].append(word)
    return word_len_dict


def longest_word(word_dictionary):
    # confirm if empty dictionary
    if not word_dictionary:
        raise ValueError("Empty word dictionary. Please load dictionary with"
                         "word length as key and associated word as value then try again")
    if not all(key is not None and value is not None for key, value in word_dictionary.items()):
        raise ValueError('Invalid dictionary, please confirm is all have corresponding keys')
    if not all(isinstance(key, int) for key in word_dictionary.keys()):
        raise TypeError("All dictionary keys must be integers denoting length of associated word")
    # identify longest key - longest word length
    max_length = max(word_dictionary.keys())

    # return longest key and word corresponding to longest key
    return max_length, word_dictionary[max_length]


if __name__ == '__main__':
    words = ["apple", "banana", "cherry", "blueberry", "Blueberry", "Clueberry"]
    word_length_dictionary = length_list(words)
    print(f"Counted words: {word_length_dictionary}")
    longest_length, longest_string = longest_word(word_length_dictionary)
    print(f"Longest word is {longest_string} and had word length of {longest_length}")
