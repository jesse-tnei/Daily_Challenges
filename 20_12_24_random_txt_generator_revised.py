import string
import random


def validate_string_length(length):
    if length <= 0:
        raise ValueError('String length must be greater than 0')


def validate_file_name(filename):
    if not filename.endswith('.txt'):
        raise ValueError('Invalid name. Filename must end with .txt')


def string_generator(length):
    """Generates a string random letters, digits and special character of length as defined by user"""

    character_pool = string.ascii_letters + string.digits + string.punctuation
    validate_string_length(length)
    return ''.join(random.choice(character_pool) for _ in range(length))


def txt_file_generator(filename, contents):
    """Creates a txt file, writes contents onto it and saves it in the same folder as the program file"""
    validate_file_name(filename)
    with open(filename, 'w') as file:
        file.write(contents)
    print(f'File {filename} has been successfully created')
    return None


def main():
    """Main function to drive the program - generates random string and writes it to a text file"""
    try:
        length = 0
        filename = 'random_file.txt'

        # create the random string
        random_string = string_generator(length)
        print(f'Generated random string {random_string}')

        # write the random string to a txt file
        txt_file_generator(filename, random_string)
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
