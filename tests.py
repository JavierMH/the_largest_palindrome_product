#!/usr/bin/env python

import unittest
from unittest.mock import patch
from the_largest_palindrome_product import LargestPalindromeProduct


class ContainersTestCase(unittest.TestCase):
    def test_get_input_stacks_processed_input_correctly(self):
        user_input = [
            2,
            101110,
            800000,
        ]
        expected_stacks = [
            101101,
            793397
        ]
        with patch('builtins.input', side_effect=user_input):
            stacks = LargestPalindromeProduct().run()
        self.assertEqual(stacks, expected_stacks)

    def test_obtain_T_by_input(self):
        T_isnt_a_digit_value = "50a"
        T_more_than_permited = 101
        T_less_than_permited = 0
        T_in_a_correct_range = 50

        with self.assertRaises(ValueError):
            LargestPalindromeProduct().constraint_for_number_of_test_cases(
                T_isnt_a_digit_value
            )
        with self.assertRaises(ValueError):
            LargestPalindromeProduct().constraint_for_number_of_test_cases(
                T_more_than_permited
            )
        with self.assertRaises(ValueError):
            LargestPalindromeProduct().constraint_for_number_of_test_cases(
                T_less_than_permited
            )
        self.assertIsNone(
            LargestPalindromeProduct().constraint_for_number_of_test_cases(
                T_in_a_correct_range
            ),
            None
        )


if __name__ == '__main__':
    unittest.main()
