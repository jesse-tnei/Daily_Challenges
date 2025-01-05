
import a_02_01_25_Billing_System as billing

def main():
    """
    The main entry point of the program.

    This function displays available items, gets user input, calculates the total cost,
    and prints the result.

    Returns:
        None
    """

    # Display available items
    item_display = billing.ItemDisplay(billing.ITEM_PRICES, 
                               'What item would you like to buy? Type item from above list here: ', 
                               'How many would you like to buy? Type the number as a digit here: ')
    item_display.display_items()

    # Get user input
    purchased_item, number = item_display.get_user_input()

    # Convert purchased item into enum value
    try:
        purchased_item = billing.PurchasableItems[purchased_item.upper()]
    except KeyError:
        print('Invalid item. Please try again.')
        exit(1)

    # Calculate total cost
    calculator = billing.ItemDisplay.TotalCostCalculator(billing.ITEM_PRICES)
    try:
        total_cost = calculator.total_cost(purchased_item, int(number))
    except ValueError:
        print('Invalid number. Please try again.')
        exit(1)

    # Display total cost
    print(f'Total cost of {number} {purchased_item.value} is ${total_cost}')

if __name__ == '__main__':
    main()
    