import unittest
from Array_Python import *

class Testset(unittest.TestCase):
    # create an empty set and check size =0
    def test_empty_set(self):
         b = create_array(3)
         check_if_empty(b) 
         assert get_size(b) ==  0

    def test_add_one_item(self):
         b = create_array(3) 
         add_item(b, 1)
         assert get_size(b) == 1

    def test_add_2_different_item(self):
        b = create_array(3)
        add_item(b, 1)
        add_item(b, 2)
        assert get_size(b) == 2

    def test_same_item(self):
        b = create_array(3) 
        add_item(b, 1)
        add_item(b, 2)
        add_item(b, 1)
        assert get_size(b) == 2

    def test_different_item_length_of_array(self):
         b = create_array(3) 
         add_item(b, 1)
         add_item(b, 2)
         add_item(b, 3)
         assert get_size(b) == 3 
   
    def test_different_item_out_of_boundary_array(self):
        b = create_array(1) 
        add_item(b, 1)
        add_item(b, 2)
        assert get_size(b) == 2 
   
    def test_remove_exist_item_from_array(self):
        b = create_array(4) 
        add_item(b, 1)
        add_item(b, 2)
        add_item(b, 3)
        remove_item(b, 1)
        assert get_size(b) == 2  
   
    def test_remove_item_which_not_exist_from_array(self):
        b = create_array(4) 
        add_item(b, 1)
        add_item(b, 2)
        add_item(b, 3)
        remove_item(b, 4)
        assert get_size(b) == 3  

if __name__ == '__main__':
    unittest.main()