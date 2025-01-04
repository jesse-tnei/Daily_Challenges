import random

FILEPATH = 'names.txt'


def random_name_gen(filepath):
    """ Loops through a list of names in a text file and returns a random name from the list
    :param
    filepath (str) system path to the txt file that is to be loaded

    :return
    the random name from the list of names

    :raises
        FileNotFoundError is the txt file provided is not present in the system or if invalid filepath has been provided
        ValueError if the file contains no valid names

    Error handling reference video: https://www.youtube.com/watch?v=NIWwJbo-9_8&ab_channel=CoreySchafer

    """
    try:
        with open(filepath, 'r') as item:
            contents = [line.strip() for line in item.readlines() if line.strip()]
        if not contents:
            raise ValueError('The file is empty, please try a different file')

        return random.choice(contents)
    except FileNotFoundError:
        print('Error, file not found. Check filepath and try again')
        return None
    except ValueError as e:
        print(f'Error{e}')
        return None


print((random_name_gen(FILEPATH)))
