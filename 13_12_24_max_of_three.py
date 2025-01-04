def largest_of_three(a=None, b=None, c=None):
    """
    Compares between three different integer inputs to identify the largest of them all.

    :param
        a int first integer argument for comparison. Initialised to None until user provides input for update
        b int second integer argument for comparison. Initialised to None until user provides input for update
        c int third integer argument for comparison. Initialised to None until user provides input for update

    :returns
        str prints statement to inform user the biggest of the three input arguments

    :raises
        TypeError if function is called with less than three input arguments or if any argument is not an integer
    """

    # Check if all three arguments are provided
    if None in [a, b, c]:  # Check if any argument is None
        raise TypeError('Function requires 3 input arguments, not enough given')

    # Check to confirm if all arguments are integers. Note that the isinstance is a built-in method in Python to check
    # The data type
    # Additionally, the use of () means that we have a generator comprehension, almost like list comprehension
    # the all is also an in-built python function that returns a true if all the generator's output meet the condition
    # note also that isinstance can take a single classtype or a tuple of class types
    if not all(isinstance(arg, (int, float)) for arg in [a, b, c]):
        raise TypeError('All arguments must be integers, not strings or other types')

    # Compare the numbers and print the largest
    if a >= b and a >= c:
        print(f'{a} is the largest of the three')
    elif b >= a and b >= c:
        print(f'{b} is the largest of the three')
    else:
        print(f'{c} is the largest of the three')


# Example usage
largest_of_three(10000, 1000.5, 100000)
