from enum import Enum
from abc import ABC, abstractmethod


class PurchasableItems(Enum):
    BUTTER: str = 'Butter'
    EGGS: str = 'Eggs'
    SALT: str = 'Salt'
    FLOUR: str = 'Flour'
    CHOCOLATE: str = 'Chocolate'
    FRIES: str = 'Fries'


# dictionary for purchasable item prices
ITEM_PRICES = {
    PurchasableItems.BUTTER: 10,
    PurchasableItems.FLOUR: 20,
    PurchasableItems.SALT: 3,
    PurchasableItems.EGGS: 6,
    PurchasableItems.CHOCOLATE: 12,
    PurchasableItems.FRIES: 10
}


class PriceRetrievalInterface(ABC):
    """Abstract class to allow for retrieving item prices"""

    @abstractmethod
    def get_price(self, item):
        pass


class PriceUpdateInterface(ABC):
    """Abstract class to allow for updating item prices"""

    @abstractmethod
    def update_price(self, item, new_price):
        pass


class ItemDisplay:
    def __init__(self, prices_dictionary):
        self.prices = prices_dictionary

    def display_items(self):
        print('Available items')
        for item, price in self.prices.items():
            print(f"{item.value}: ${price}")

