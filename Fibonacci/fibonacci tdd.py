import unittest

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list

class TestFibonacci(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fibonacci(0), [])

    def test_one(self):
        self.assertEqual(fibonacci(1), [0])

    def test_two(self):
        self.assertEqual(fibonacci(2), [0, 1])

    def test_three(self):
        self.assertEqual(fibonacci(3), [0, 1, 1])

    def test_ten(self):
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == '__main__':
    unittest.main()