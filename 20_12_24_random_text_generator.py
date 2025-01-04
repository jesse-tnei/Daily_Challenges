import string
import random

STRING_LENGTH = 10
FILENAME = 'random_txt_file.txt'


def string_generator():
    """
    Generates a string of random letters, digits and special characters of length as defined by the user

    :param
        STRING_LENGTH int
            The total number of characters the user wishes the generated string to have
    :return:
        string_to_write str
            the string of random characters
    """
    character_pool = string.ascii_letters + string.digits + string.punctuation
    if STRING_LENGTH <= 0:
        print('Invalid argument, string length must be greater than one')
    string_to_write = ''.join(random.choice(character_pool) for _ in range(STRING_LENGTH))
    return string_to_write


print(string_generator())


def txt_file_generator():
    """
    Creates txt file, opens it in read mode and write contents onto the file then saves it
    :param
        FILENAME str
            The name to be used when saving the txt file.
            Note, this must end with .txt
    :return:
        None
        Instead, creates the new txt file and saves it under the same folder as the script
    """
    if not FILENAME[-4:] == '.txt':
        print('Invalid filename extension type. Please make sure filename ends with .txt')

    else:
        with open(FILENAME, 'w') as item:
            item.write(string_generator())
            item.close()
    return


txt_file_generator()
