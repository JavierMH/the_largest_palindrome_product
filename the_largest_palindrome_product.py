#!/usr/bin/env python


class LargestPalindromeProduct():
    def get_the_largest_palindrome_product(self, maximun_limit):
        the_largest_palindrome = 0
        for factor_1 in range(100, 1000):
            for factor_2 in range(factor_1, 1000):
                product = factor_1 * factor_2
                if str(product) == str(product)[::-1]:
                    if (product <= maximun_limit and
                            product >= the_largest_palindrome):
                        the_largest_palindrome = product
        print(the_largest_palindrome)
        return the_largest_palindrome

    def constraint_for_number_of_test_cases(self, number_of_test_cases):
        if isinstance(number_of_test_cases, str):
            if not number_of_test_cases.isdigit():
                raise ValueError(
                    '\nPlease enter an integer number!\n'
                )
            number_of_test_cases = int(number_of_test_cases)
        if number_of_test_cases > 100 or number_of_test_cases < 1:
            raise ValueError(
                '\nPlease enter an integer number between 1 and 100\n'
            )

    def _obtain_number_of_test_cases_by_input(self):
        while True:
            number_of_test_cases = input('Enter T\n>>>> ')
            try:
                self.constraint_for_number_of_test_cases(
                    number_of_test_cases
                )
            except ValueError as ve:
                print(ve)
                continue
            number_of_test_cases = int(number_of_test_cases)
            return number_of_test_cases

    def run(self):
        number_of_test_cases = (
            self._obtain_number_of_test_cases_by_input()
        )
        the_largest_palindrome_list = []
        for i in range(number_of_test_cases):
            maximun_limit = int(input('Enter N\n>>>> '))
            the_largest_palindrome_list.append(
                self.get_the_largest_palindrome_product(maximun_limit)
            )

        return the_largest_palindrome_list


if __name__ == '__main__':
    LargestPalindromeProduct().run()
