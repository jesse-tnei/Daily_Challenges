def weather_check():
    """ Provides the user with activity recommendation depending on weather type as specified by user

    Parameters
    __________
    number: str
         string input - must be a digit between 1 and 3 to allow user to select weather type

    Returns
    _______
    String message recommending user activity from existing dictionary


    Raises
    ______
    ValueError: 'Invalid input, please enter integer number' if user enters string instead of digit input
    KeyError: 'Invalid input, the number of your weather choice does not exist in database. Try again' if user enters string outside dictionary range
    """

    # Dictionary for user recommendations
    weather_activities = {
        '1': 'Its a beautiful day! How about a walk in the park?',
        '2': 'Perfect weather for a cozy indoor day with a good book',
        '3': 'Maybe its a great time for a reflective cup of tea',
        '4': 'Build a snowman or have a snowball fight'
    }

    # List for weather types
    weather_types = ['Sunny', 'Rainy', 'Cloudy', 'Snowy']

    # Standard display message for weather options
    print('What is the weather like today?')
    for i, weather_type in enumerate(weather_types):
        print(f'{i + 1}. {weather_type}')

    # User prompt
    while True:
        user_input = input("Choose 1, 2, 3 or 4: ").strip()

        if not user_input.isdigit():
            print('Invalid input, please enter a digit number e.g., 7')
            continue
        # We don't need to include .keys() because the in directly checks the keys in the dictionary
        elif user_input in weather_activities:
            return weather_activities[user_input]
        else:
            print('Number outside range, please enter digit between 1 and 4')


print(weather_check())
