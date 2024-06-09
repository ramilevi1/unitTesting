from unittest import mock
from unittest.mock import patch
from multipleQuestion import *
import unittest

class Testset(unittest.TestCase):  
    def test_zero_correct(self):
        lst = ["a","b","c", "b"]
        assert run_quiz(lst) == 0

    def test_only_one_correct(self):
        lst = ["b","c","c","a"]
        assert run_quiz(lst) == 1

    def test_only_two_correct(self):
        lst = ["b","b","b","c"]
        assert run_quiz(lst) == 2

    def test_all_correct(self):
        lst = ["b","a","a","c"]
        self.assertEqual(run_quiz(lst), 4)

    @mock.patch('multipleQuestion.get_user_input', return_value=['b','a','b','c'])
    def test_user_input(self, mock_user_input):      
        lst = mock_user_input(data)
        self.assertTrue(lst)

    
    @mock.patch('multipleQuestion.get_user_input',return_value=['b','a','b','c'])
    def test_user_input2(self, mock_user_input):
        lst1 = mock_user_input(data)
        self.assertEqual(run_quiz(lst1),3)

if __name__ == '__main__':
    unittest.main()