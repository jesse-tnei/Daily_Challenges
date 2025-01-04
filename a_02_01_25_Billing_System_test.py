import unittest
from enum import Enum
from a_02_01_25_Billing_System import PurchasableItems, ITEM_PRICES


class TestPurchasableItems(unittest.TestCase):
    """Slightly more unique class in that we are not checking methods but attributes
    In that sense, we don't see input/output but more attribute retrieval etc"""

    def test_enum_members_exist(self):
        """Confirms that the instantiated class attribute exists"""
        self.assertTrue(hasattr(PurchasableItems, "BUTTER"))
        self.assertTrue(hasattr(PurchasableItems, "EGGS"))
        self.assertTrue(hasattr(PurchasableItems, "SALT"))
        self.assertTrue(hasattr(PurchasableItems, "FLOUR"))
        self.assertTrue(hasattr(PurchasableItems, "CHOCOLATE"))
        self.assertTrue(hasattr(PurchasableItems, "FRIES"))

    def test_enum_member_values_assigned(self):
        """Confirm that the dict.value maps to the string in PurchasableItems class"""
        self.assertEqual(PurchasableItems.BUTTER.value, 'Butter')
        self.assertEqual(PurchasableItems.FLOUR.value, 'Flour')
        self.assertEqual(PurchasableItems.SALT.value, 'Salt')
        self.assertEqual(PurchasableItems.EGGS.value, 'Eggs')
        self.assertEqual(PurchasableItems.CHOCOLATE.value, 'Chocolate')
        self.assertEqual(PurchasableItems.FRIES.value, 'Fries')

    def test_enum_member_accessible(self):
        """Confirms that if we were to call that attribute, it would be returned"""
        self.assertIsInstance(PurchasableItems.BUTTER, PurchasableItems)
        self.assertIsInstance(PurchasableItems.FLOUR, PurchasableItems)
        self.assertIsInstance(PurchasableItems.SALT, PurchasableItems)
        self.assertIsInstance(PurchasableItems.EGGS, PurchasableItems)
        self.assertIsInstance(PurchasableItems.CHOCOLATE, PurchasableItems)
        self.assertIsInstance(PurchasableItems.FRIES, PurchasableItems)

    def test_enum_iteration(self):
        """Confirms if member list is iterable. Note, the expected items must be in same order as when defined"""
        items = [item for item in PurchasableItems]
        expected_items = [
            PurchasableItems.BUTTER,
            PurchasableItems.EGGS,
            PurchasableItems.SALT,
            PurchasableItems.FLOUR,
            PurchasableItems.CHOCOLATE,
            PurchasableItems.FRIES,
        ]
        self.assertEqual(items, expected_items)

    def test_unique_enum_member_values(self):
        """Checks for uniqueness of member item values through the use of list-to-set conversion which removes
        duplicates"""
        item_values = [item.value for item in PurchasableItems]
        self.assertEqual(len(item_values), len(set(item_values)))

    def test_enum_member_values_capitalised(self):
        """Ensures all the string values, when instantiated, are capitalised"""
        item_values = [item.value for item in PurchasableItems]
        expected_item_values = [item.capitalize() for item in item_values]
        self.assertEqual(item_values, expected_item_values)


class TestItemPrices(unittest.TestCase):
    def test_item_price_key_in_enum(self):
        """Confirm keys in dictionary are present in the enum class
         Reminds developer that every time they update the PurchasableItems class,
         they need to update the ITEM_PRICES dictionary too"""
        for key in ITEM_PRICES.keys():
            self.assertIn(key, PurchasableItems)

    def test_item_price_is_positive_integer(self):
        """Confirms price is integer or float and greater than 0 i.e., positive"""
        for value in ITEM_PRICES.values():
            self.assertIsInstance(value, (int, float))
            self.assertGreater(value, 0)

    def test_item_price_dict_key_value_pair_match(self):
        """Confirm if dictionary is not empty then compare to ensure each key has a
        value associated with it
        by checking the length of key and value lists"""
        self.assertTrue(len(ITEM_PRICES)>0)
        keys = [key for key in ITEM_PRICES.keys()]
        values = [value for value in ITEM_PRICES.values()]
        self.assertEqual(len(keys), len(values))

    def test_all_items_have_prices(self):
        """Ensures every PurchasableItem is a key in ITEM_PRICES
        and that it has an associated price"""
        for item in PurchasableItems:
            self.assertIn(item, ITEM_PRICES)
            self.assertIsNotNone(ITEM_PRICES[item])


if __name__ == '__main__':
    unittest.main()
