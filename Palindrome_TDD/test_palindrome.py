import unittest
from solution_palindrome import *

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome_with_empty_string(self):
        assert is_palindrome('') is True  # special case  

    def test_is_palindrome_with_one_char(self):
        assert is_palindrome('A') is True
        assert is_palindrome('C') is True

    def test_is_palindrome_with_two_char_false(self):
        assert is_palindrome('AB') is False

    def test_is_palindrome_with_two_char(self):
        assert is_palindrome('AA') is True

    def test_is_palindrome_with_mix_cases(self):
        assert is_palindrome('Aa') is True

    def test_is_palindrome_with_withspace(self):    
        assert is_palindrome('Race cAr') is True

    def test_is_palindrome_with_withspaces(self):    
        assert is_palindrome('race fast safe car') is True

    def test_is_palindrome_with_numbers(self):
        assert is_palindrome('12321 12321') is True

    def test_is_palindrome_with_punctuation(self):
        assert is_palindrome('Race, cAr') is True
        assert is_palindrome('Race, cAr!') is True

    def test_is_palindrome_with_pforeign_languages(self):    
         assert is_palindrome('Ce repère, Perec') is True
         assert is_palindrome('Trug Tim eine so helle Hose nie mit Gurt?') is True
         assert is_palindrome('Tu l’as trop ecrase cesar ce port salut.') is True

    def test_is_palindrome_very_long(self):
        assert is_palindrome('Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.') is True
        assert is_palindrome('Are we not drawn onward, we few, drawn onward to new era? Are we not drawn onward, we few, drawn onward to new era?') is True
    
    def test_is_palindrome_punctuation(self):
        self.assertTrue(is_palindrome('a,b$b,a')) 

   
if __name__ == '__main__':
    unittest.main()
