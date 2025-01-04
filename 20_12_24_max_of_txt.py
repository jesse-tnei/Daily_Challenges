def load_contents(filepath):
    """Checks to see if given filepath is valid then loads contents
    :param
        filepath str
            path to the file which is to be loaded
    :raise
        FileNotFoundError if the file does not exist or path is invalid"""
    try:
        with open(filepath, 'r') as file:
            contents = file.readlines()
        print(f'File {filepath} successfully loaded')
        return contents
    except:
        raise FileNotFoundError('File not found, check filepath again')


def validate_list(list_of_items):
    """Helper function to confirm that the contents loaded are in the form of a list"""
    if len(list_of_items) <= 0:
        raise ValueError('List has no elements')
    # feedback from GPT - this is too small a function
    # Since its tightly coupled with loading contents, we can include both of them under the same banner


def content_cleaner(contents):
    """Takes input, confirms if it's of list type then converts the list elements into integer type
    :param
        contents list
            the list whose contents are to be converted to integer
    :raise
        ValueError if contents parameter is not a list
    :returns
        list of integer elements"""
    validate_list(contents)

    return [int(i.strip('\n')) for i in contents]


def maximum(list_of_numbers):
    """
    Takes a list of integer elements and converts returns the maximum of the elements
    :param
        list_of_numbers: list of ints
    :return:
        int maximum value from the list
    """
    return max(list_of_numbers)

    # Feedback from GPT - max is an inbuilt python function, no point in calling it under a separate function
    # especially if its the only thing running under this hood


def main():
    """Main function to drive the whole process"""
    try:
        filepath = 'numbers.txt'
        raw_list = load_contents(filepath)
        cleaned_list = content_cleaner(raw_list)
        print(f'Cleaned list contains elements {cleaned_list}')
        return max(cleaned_list)
    except ValueError as e:
        print(f'Error {e}')


if __name__ == '__main__':
    print(f'Maximum number is {main()}')
