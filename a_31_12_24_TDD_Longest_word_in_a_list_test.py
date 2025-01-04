import unittest
from a_31_12_24_TDD_Longest_word_in_a_list import length_list, longest_word


class TestLongestItemInList(unittest.TestCase):
    def test_length_list_raises_error_on_non_list_input(self):
        # integer input
        with self.assertRaises(TypeError):
            length_list(1)

        # string input
        with self.assertRaises(TypeError):
            length_list('apple')

    def test_length_list_raises_error_on_empty_list(self):
        with self.assertRaises(ValueError):
            length_list([])

    def test_length_list_raises_error_on_non_string_list_elements(self):
        with self.assertRaises(ValueError):
            length_list(["apple", '3', True, ""])

    def test_length_list_on_pure_string_list_with_varying_lengths(self):
        self.assertEqual(length_list(["apple", "banana", "cherry", "blueberry"]),
                         {5: 'apple', 6: 'banana', 6: 'cherry', 9: 'blueberry'})

    def test_length_list_on_pure_string_list_with_equal_lengths(self):
        self.assertEqual(length_list(["apple", "apple", "apple", "apple"]),
                         {5: 'apple', 5: 'apple', 5: 'apple', 5: 'apple', 5: 'apple'})

    def test_longest_word_with_expected_dictionary(self):
        # set up operation for expected output
        input_dict = {5: 'apple', 6: 'cherry', 9: 'blueberry'}
        longest_length, longest_string = longest_word(input_dict)
        expected_output = (9, 'blueberry')

        # check to confirm actual output is same as expected output
        self.assertEqual((longest_length, longest_string), expected_output)

    def test_longest_word_with_empty_dictionary(self):
        # empty dictionary
        with self.assertRaises(ValueError):
            longest_word({})

        # invalid dictionary
        with self.assertRaises(ValueError):
            longest_word({5: 'apple', 6: 'cherry', None: 'blueberry'})

    def test_longest_word_with_string_keys_in_input_dictionary(self):
        with self.assertRaises(TypeError):
            longest_word({'five': 'apple', 'six': 'cherry', 'nine': 'blueberry'})


if __name__ == '__main':
    unittest.main()
