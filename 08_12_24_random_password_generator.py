import secrets
import string

MINIMUM_PASSWORD_LENGTH = 6


def get_password_parameters():
    """
    Gathers and validates user input for password specifications.

    :return:
    A dictionary containing password parameters.
    """
    print('Welcome to the Password Generator!')
    while True:
        try:
            password_length = int(input(f'Enter desired password length (minimum {MINIMUM_PASSWORD_LENGTH}): ').strip())
            if password_length < MINIMUM_PASSWORD_LENGTH:
                print(f'Password length must be at least {MINIMUM_PASSWORD_LENGTH}. Please try again.')
                continue
        except ValueError:
            print('Invalid input. Please enter a valid number for the password length.')
            continue

        # Collect user choices
        include_uppercase = input('Include uppercase letters? (yes/no): ').strip().lower()
        include_numbers = input('Include numbers? (yes/no): ').strip().lower()
        include_special_chars = input('Include special characters? (yes/no): ').strip().lower()

        # Ensure at least one character set is selected
        if include_uppercase == 'no' and include_numbers == 'no' and include_special_chars == 'no':
            print('You must select at least one character type. Please try again.')
            continue

        # Return validated parameters
        return {
            'length': password_length,
            'uppercase': include_uppercase == 'yes',
            'numbers': include_numbers == 'yes',
            'special_chars': include_special_chars == 'yes'
        }


def generate_password(params):
    """
    Generates a secure random password based on the provided parameters.

    :param params: Dictionary containing password parameters.
    :return: A randomly generated password as a string.
    """
    # Start with lowercase letters as the base character set
    character_pool = string.ascii_lowercase
    if params['uppercase']:
        character_pool += string.ascii_uppercase
    if params['numbers']:
        character_pool += string.digits
    if params['special_chars']:
        character_pool += string.punctuation

    # Generate the password
    return ''.join(secrets.choice(character_pool) for _ in range(params['length']))


# Main program flow
if __name__ == "__main__":
    user_params = get_password_parameters()
    secure_password = generate_password(user_params)
    print(f'Your secure password is: {secure_password}')
