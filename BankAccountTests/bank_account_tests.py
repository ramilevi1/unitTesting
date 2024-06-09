import io
import unittest
from unittest import mock
from unittest.mock import patch
from bank_account import *

class Testset(unittest.TestCase):
    def test_create_new_account(self):
         newAccount = BankAccount(2178514584, "Rami" , 2700)
         assert newAccount.name ==  'Rami'
         assert newAccount.balance ==  2700

    def test_display_account_info(self):
        newAccount = BankAccount(2178514584, "Rami" , 2700) 
        self.assertTrue(newAccount.display)

    def test_create_withdrawal_with_fees(self):
        newAccount = BankAccount(2178514584, "Rami" , 3200) 
        newAccount.Withdrawal(200)
        assert newAccount.balance == 3000*0.95
          
    def test_create_negative_withdrawal_with_fees(self):
        newAccount = BankAccount(2178514584, "Rami" , 3200) 
        newAccount.Withdrawal(3300)
        assert  newAccount.balance == -100*1.1

    def test_create_negative_withdrawal_with_fees(self):
        newAccount = BankAccount(2178514584, "Rami" , 3200) 
        newAccount.Withdrawal(6400)
        assert  newAccount.balance == 3200

    def test_create_deposit(self):
        newAccount = BankAccount(2178514584, "Rami" , 2700) 
        newAccount.Deposit(300)
        assert newAccount.balance ==  3000

    def test_combine_account(self):
        newAccount = BankAccount(2178514584, "Rami" , 2700) 
        newForiegnAccount = BankForiengAccount(2178514584, "Rami" , 2300, "Euro")
        if newForiegnAccount.accountNumber == newAccount.accountNumber:
           newAccount.balance = newForiegnAccount.combinedAccountInfo(newForiegnAccount, newAccount)
        assert newAccount.balance ==  5092.0

    # #mocking the returnvalue function (return function and validating arg including number of func call=1)
    @patch('bank_account.BankAccount.returnValue')
    def test_func(self, get_content_mock):
        get_content_mock.return_value = 2700
        my_class= BankAccount.returnValue()
        self.assertEqual(my_class, 2700)
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()

class Testset2(unittest.TestCase):
    # #mocking the withrawal function (no return function and validating arg including number of func call=1)
    @patch('bank_account.BankAccount.Withdrawal')
    def test_func(self, mock_bar):
         mock_bar(2000)
         self.assertTrue(mock_bar)
         self.assertEqual(mock_bar.call_args[0][0], 2000)
         self.assertEqual(mock_bar.call_count, 1)

class Testset3(unittest.TestCase):
 @patch('bank_account.BankAccount.returnValue')
 def test_func(self, get_content_mock):
        get_content_mock.return_value = 2700
        my_class= BankAccount.returnValue()
        self.assertEqual(my_class, 2700)
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()
   
if __name__ == '__main__':
    unittest.main()