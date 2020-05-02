import unittest
from Fizzbuzz import Fizzbuzz


class FizzbuzzTest(unittest.TestCase):

    def test_fizz_condition(self):
        fizzbuzz = Fizzbuzz()
        response = fizzbuzz.calculate(3)
        self.assertEqual('Fizz', response)

    def test_buzz_condition(self):
        fizzbuzz = Fizzbuzz()
        response = fizzbuzz.calculate(5)
        self.assertEqual('Buzz', response)

    def test_if_number_is_fizz_and_buzz(self):
        fizzbuzz = Fizzbuzz()
        response = fizzbuzz.calculate(15)
        self.assertEqual ('FizzBuzz', response)

    def test_number_not_fizz_or_buzz(self):
        fizzbuzz = Fizzbuzz()
        response = fizzbuzz.calculate(7)
        self.assertEqual(7,response)


if __name__ == '__main__':
    unittest.main()
