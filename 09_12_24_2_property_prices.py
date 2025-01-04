CITY_PRICE_PER_SQFT = 250
SUBURB_PRICE_PER_SQFT = 150


def property_prices():
    """
    prints total property prices in dollars depending on property size and location

    :param:
        property_size (str converted to int)
            digit type user input to define the size of the property in square feet
        property_location (str)
            either suburb or city location as defined by user
    :return:
        string message printout indicating the property prices - prices per square feet* size in square feet depending
        on property location

    :raises
        warning message if user provides non-digit number for property size
    """
    print('Welcome to the Real Estate Price Estimator')
    while True:
        property_size = input('Enter the size of the property as an integer in square feet. For example '
                              '2000 sqft would be entered as 2000. Type q and press Enter to quit: ').strip()

        if not property_size.isdigit():
            if property_size.lower() == 'q':
                print('Session closed')
                exit()
            else:
                print('Please enter value as digit instead of string')
                continue

        property_location = input('Enter the location (city or suburb): ').strip().lower()

        match property_location:
            case 'city':
                print(
                    f"Calculated price for {property_size} sqft property in the {property_location} is ${int(property_size) * CITY_PRICE_PER_SQFT}")
            case 'suburb':
                print(
                    f"Calculated price for {property_size} sqft property in the {property_location} is ${int(property_size) * SUBURB_PRICE_PER_SQFT}")
            case _:
                print('Invalid location, please try again')
                continue


property_prices()
