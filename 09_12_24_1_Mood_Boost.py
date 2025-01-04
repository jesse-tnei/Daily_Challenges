def mood_boost():
    """
    Prints out different string message types depending on user mood as input

    :param: username (str), user_mood (str)
    :return: message (str) depending on user mood choice

    """

    user_name = input('Hello, what is your name? ')
    while True:
        print(f'Hi, {user_name}! How are you feeling today?')
        mood_list = ['Happy', 'Stressed', 'Tired']
        for i, mood in enumerate(mood_list):
            print(f'{i + 1}. {mood}')

        user_mood = input('Choose 1,2 or 3. Type q and press enter to quit: ').strip()

        if user_mood == 'q':
            break

        if not user_mood.isdigit():
            print('Invalid input, please enter a digit number and not a string')
            continue
        else:
            match user_mood:
                case '1':
                    print(f"That's great {user_name}! Keep spreading your joy")

                case '2':
                    print(f"Take a deep breath {user_name}. You're doing amazing!")

                case '3':
                    print(f"Rest up {user_name}. Tomorrow is a fresh start!")
                case _:
                    print('The number you entered is out of range, please try again')
                    continue
        break
    return 0


if __name__ == '__main__':
    mood_boost()
