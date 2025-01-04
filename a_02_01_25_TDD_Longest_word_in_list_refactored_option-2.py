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


def longest_grouped_word(grouped_words, key_func=lambda x: x):
    # key_func is the mapping function
    # note that by default, this has been set to map the key to itself
    # such that if the dictionary key is the integer of the length of words,
    # then we do direct mapping
    if not isinstance(grouped_words, dict):
        raise TypeError("Input must be a dictionary")
    if not all(isinstance(key_func(key), int) and isinstance(value, list) for key, value in grouped_words.items()):
        raise ValueError("Keys must map to integers, and values must be lists")

    max_key = max(grouped_words.keys(), key=key_func)
    return max_key, grouped_words[max_key]


if __name__ == '__main__':
    words = ["apple", "banana", "cherry", "blueberry", "Blueberry", "Blueberry"]
    word_length_dictionary = length_list(words)
    print("Word length dictionary:")
    for length, word_list in word_length_dictionary.items():
        print(f"Length {length}: {word_list}")
    longest_length, longest_strings = longest_grouped_word(word_length_dictionary)
    print(f"The longest word(s) are {longest_strings} with a length of {longest_length}.")

    # alternative usage of the longest_grouped_word function
    letter_groups = {'a': ['apple'], 'b': ['banana', 'blueberry']}
    print(longest_grouped_word(letter_groups, key_func=lambda x: len(x)))