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

    def run(self):
        number_of_test_cases = int(input('Enter T\n>>>> '))
        if number_of_test_cases > 100 and number_of_test_cases < 1:
            raise ValueError()
        the_largest_palindrome_list = []
        for i in range(number_of_test_cases):
            maximun_limit = int(input('Enter N\n>>>> '))
            the_largest_palindrome_list.append(
                self.get_the_largest_palindrome_product(maximun_limit)
            )

        return the_largest_palindrome_list


if __name__ == '__main__':
    LargestPalindromeProduct().run()
