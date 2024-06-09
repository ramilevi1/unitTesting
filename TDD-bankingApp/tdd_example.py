
import unittest
from banking_app import Banking
class Tdd_Python(unittest.TestCase):
 def test_banking_credit_method_returns_correct_result(self):
     bank = Banking()
final_bal = Banking.credit(1000)
self = None
self.assertEqual(1000, final_bal)
if __name__ == '__main__':
 unittest.main()