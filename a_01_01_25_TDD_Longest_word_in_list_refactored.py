from collections import defaultdict


def validate_list(input_list):
    # confirm input present
    if not input_list:
        raise ValueError('Input is an empty list')

    # confirm input is a list
    if not isinstance(input_list, list):
        raise TypeError('Input not a list, please try again')

    # confirm all input elements are string type
    if not all(isinstance(word, str) for word in input_list):
        raise ValueError('List contains non-string elements')


def validate_input_dictionary(input_dictionary):
    # confirm if empty dictionary
    if not input_dictionary:
        raise ValueError("Empty word dictionary. Please load dictionary with"
                         "word length as key and associated word as value then try again")

    # check for None elements in the input dictionary
    if not all(key is not None and value is not None for key, value in input_dictionary.items()):
        raise ValueError('Invalid dictionary, please confirm is all have corresponding keys')

    # ensure all the keys are integers
    if not all(isinstance(key, int) for key in input_dictionary.keys()):
        raise TypeError("All dictionary keys must be integers denoting length of associated word")

    # ensure all values are lists of strings
    if not all(isinstance(value, list) and all(isinstance(word, str) for word in value) for value in
               input_dictionary.values()):
        raise ValueError('All dictionary values must be lists of strings')


def length_list(word_string_list):
    # ensure that input list is valid
    validate_list(word_string_list)

    # initialise empty default dictionary
    word_len_dict = defaultdict(list)

    # zip the two lists up into a dictionary
    for word in word_string_list:
        # obtain length of each word and use it to create new key with list as the value
        word_len = len(word)
        # append the word itself to the value list. If key already created, add the word to the value list
        word_len_dict[word_len].append(word)
    return word_len_dict


def longest_word(word_dictionary):
    # validate dictionary
    validate_input_dictionary(word_dictionary)

    # identify longest key - longest word length
    max_length = max(word_dictionary.keys())

    # return longest key and word corresponding to the longest key
    return max_length, word_dictionary[max_length]


if __name__ == '__main__':
    words = ["apple", "banana", "cherry", "blueberry", "Blueberry", "Blueberry"]
    word_length_dictionary = length_list(words)
    print("Word length dictionary:")
    for length, word_list in word_length_dictionary.items():
        print(f"Length {length}: {word_list}")
    longest_length, longest_strings = longest_word(word_length_dictionary)
    print(f"The longest word(s) are {longest_strings} with a length of {longest_length}.")
