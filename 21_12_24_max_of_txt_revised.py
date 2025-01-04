import os


def load_contents(filepath):
    """Loads contents of a file line by line
    :param
        filepath str
            path to the file which is to be loaded
    :returns
        contents list
        a list of strings where each string corresponds to the line in the loaded file
    :raises
        FileNotFoundError
            If the file does not exist or the filepath is invalid"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'File {filepath} not found. Check filepath and try again')
    with open(filepath, 'r') as file:
        contents = file.readlines()
    print(f'File {filepath} loaded successfully')
    return contents


def validate_and_clean_list(contents):
    """
    Validates list and converts its elements into an integer type
    :param
        contents: list
            the individual elements within that list have now been converted into integer type
    Note: I had added the filepath as a parameter to be printed out but removed it based on the concept of modularity
    You want each function to perform one task only, and to be as independent of other elements as possible.
    For example, suppose we want to use this function to validate another list which was not loaded using the filepath?
    Including the filepath variable would make it less modular and more specific to this script
    :return: list
        contents is a list made up of integer type elements
    :raises
        ValueError
            if the input list file is empty or contains non-numeric elements which cannot be converted to integer type
    """
    if not contents:
        # raise ValueError(f'The loaded file {filepath} is empty')
        raise ValueError(f'The loaded file is empty')
    try:
        return [int(content) for content in contents]
    except ValueError:
        raise ValueError('Loaded file contains non-numeric variables that cannot be converted to integer type')


def maximum_number(numbers):
    """
    Finds and returns maximum value in a list of integers
    :param
        numbers: list
            A list containing integer values
    :return:
        maximum integer value from the list of integers

    :raises
        ValueError if there is an element within the list that is not an integer
        Note that this error is added here to make sure that this function is isolated in its operation such that
        we can use it on any other list. The idea is to promote modularity and avoid tightly coupling functions
    """
    if not numbers:
        raise ValueError('Cannot find maximum number in an empty list')
    try:
        return max(numbers)
    except ValueError:
        raise ValueError('Certain elements in numbers are non-numerical hence cannot locate maximum value')


def main(filepath):
    """
    Drives the process of loading the file, cleaning its contents and returning the maximum value in the list
    :param
    filepath: str
        string input to specify where the file to be loaded is located
    :return: int
        maximum value identified in the list
        None if any of the functions called results in an error
    :raises
        FileNotFoundError is filepath invalid
        ValueError is list is empty or contains non-numeric elements
    """
    try:
        raw_list = load_contents(filepath)
        cleaned_list = validate_and_clean_list(raw_list)
        print(f'Cleaned list: {cleaned_list}')
        return maximum_number(cleaned_list)
    except (FileNotFoundError, ValueError) as e:
        print(f'Error {e}')
        return None


if __name__ == '__main__':
    filepath = 'numbers.txt'
    max_value = main(filepath)
    if max_value is not None:
        print(f'Maximum value in the list is {max_value}')


