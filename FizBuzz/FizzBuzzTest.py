
import unittest
from FizzBuzz import *


class Testset(unittest.TestCase):
        def test_returns_fizz_With_3(self):
            assert fizzBuzz(3) == "Fizz"

        def test_returns_2_With_2(self):
            assert fizzBuzz(2) == "2"

        def test_returns_Buzz_With_5(self):
            assert fizzBuzz(5) == "Buzz"

        def test_returns_Fizz_With_6(self):
            assert fizzBuzz(6)== "Fizz"

        def test_returns_Buzz_With_10(self):
            assert fizzBuzz(10) == "Buzz"

        def test_returns_FizzBuzz_With_15(self):
            assert fizzBuzz(15)== "FizzBuzz"

        def test_returns_FizzBuzz_With_1905(self):
            assert fizzBuzz(1905)== "FizzBuzz"


if __name__ == '__main__':
    unittest.main()