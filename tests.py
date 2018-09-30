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


if __name__ == '__main__':
    unittest.main()
