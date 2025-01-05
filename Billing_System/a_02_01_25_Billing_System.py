from enum import Enum
from abc import ABC, abstractmethod


class PurchasableItems(Enum):
    """
    An enumeration of purchasable items.

    This class defines a set of constants for purchasable items, such as butter, eggs, salt, etc.
    """
    BUTTER: str = 'Butter'
    EGGS: str = 'Eggs'
    SALT: str = 'Salt'
    FLOUR: str = 'Flour'
    CHOCOLATE: str = 'Chocolate'
    FRIES: str = 'Fries'

ITEM_PRICES = {
    PurchasableItems.BUTTER: 10,
    PurchasableItems.FLOUR: 20,
    PurchasableItems.SALT: 3,
    PurchasableItems.EGGS: 6,
    PurchasableItems.CHOCOLATE: 12,
    PurchasableItems.FRIES: 10
}

class ObtainUserInputInterface(ABC):
    """Abstract class to allow for obtaining user input"""

    @abstractmethod
    def get_user_input(self):
        """
        Obtains user input from the console.

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            str: The user's input as a string.
        """
        pass

class PriceRetrievalInterface(ABC):
    """Abstract class to allow for retrieving item prices"""

    @abstractmethod
    def get_price(self, item):
        """
        Retrieves the price of a given item.

        Args:
            item (PurchasableItems): The item to retrieve the price for.

        Returns:
            float: The price of the item.
        """
        pass




class PriceUpdateInterface(ABC):
    """Abstract class to allow for updating item prices"""

    @abstractmethod
    def update_price(self, item, new_price):
        """
        Updates the price of a given item.

        Args:
            item (PurchasableItems): The item to update the price for.
            new_price (float): The new price of the item.
        """
        pass

class ItemDisplay(ObtainUserInputInterface):
    """
    A class to display available items and their prices.

    Attributes:
        prices (dict): A dictionary of items and their prices.
    """
    def __init__(self, prices_dictionary, purchased_item_prompt, number_prompt):
        """
        Initializes the ItemDisplay class with a dictionary of items and their prices.

        Args:
            prices_dictionary (dict): A dictionary of items and their prices.
            purchased_item_prompt (str): The prompt to ask the user for the item they want to purchase.
            number_prompt (str): The prompt to ask the user for the number of items they want to purchase.
        """
        self.prices = prices_dictionary
        self.purchased_item_prompt = purchased_item_prompt
        self.number_prompt = number_prompt

    def display_items(self):
        """
        Displays the available items and their prices.
    
        Prints a list of items and their corresponding prices to the console.
        """
        print('Available items')
        for item, price in self.prices.items():
            print(f"{item.value}: ${price}")
            
    def get_user_input(self):
        """
        Retrieves the item and quantity from the user.

        Asks the user for the item purchased and the quantity purchased, and returns the input as a tuple of two strings.

        Returns:
            tuple: A tuple containing the item purchased and the quantity purchased.
        """
        return input(self.purchased_item_prompt).strip(), input(self.number_prompt).strip()

    class TotalCostCalculator(PriceRetrievalInterface):
        """
        A class to calculate the total cost of items.
    
        Attributes:
            prices (dict): A dictionary of items and their prices.
        """
        def __init__(self, prices_dictionary):
            """
            Initializes the TotalCostCalculator class with a dictionary of items and their prices.

            Args:
                prices_dictionary (dict): A dictionary of items and their prices.
            """
            self.prices = prices_dictionary
    
        def get_price(self, item):
            """
            Retrieves the price of a given item.
            
            Args:
                item: The item to retrieve the price for.
            
            Returns:
                float: The price of the item.
            """
            return self.prices[item]
        
        def total_cost(self, item, quantity):
            """
            Calculates the total cost of an item.
            
            Args:
                item: The item to calculate the total cost for.
                quantity: The number of items to calculate the total cost for.
            
            Returns:
                float: The total cost of the item.
            """
            return self.get_price(item) * quantity

