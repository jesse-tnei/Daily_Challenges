import re


def book_word_counter():
    """Counts the words in a text file and returns this as an integer

    Parameters
    __________
    filepath: str
        The path to the file that is to be read

    Returns
    ______
    the number of words in the file

    raises
    ______
    FileNotFoundError
        If the file does not exist in the path that has been provided

    ValueError
        If the filepath is empty or None. Prompts user to provide str input"""
    filepath = input('Enter filepath as string here, for example, book.txt: ')
    if not filepath:
        raise ValueError('Filepath not provided, please provide filepath with filename as ../filename.txt')

    try:
        with open(filepath, 'r', encoding='utf-8') as item:
            contents = item.read()
        # Note that the ^ when used with a set negates so basically replace anything that is not a-z, A-Z or 0-9 with
        # empty spaces
        # The \s is the whitespace since in this case, we want to keep that too
        clean_content = re.sub(r'[^a-zA-Z0-9\s]', '', contents)

        # .split, if with no input, would split along any kind of spaces including new lines
        # however, if we include the ' ' argument, we are then counting
        # the \n etc as individual words hence higher wordcount
        word_count = len(clean_content.split())

        return word_count
    except FileNotFoundError:
        raise FileNotFoundError('File not found, please check provided filepath again')
    except Exception as e:
        raise RuntimeError(f'An unexpected error occurred: {str(e)}')


print(f'Word count in provided text is: {book_word_counter()}')

# YOUTUBE VIDEO ON REGEX: https://www.youtube.com/watch?v=nxjwB8up2gI
