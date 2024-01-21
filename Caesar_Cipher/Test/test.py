from Caesar_Cipher.Function.caesar_cipher import get_caesarCipher
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_Lipps_Asvph (self): 
        n = 12
        s = 'Hello_World!'
        k = 4
        result = get_caesarCipher(s, k)
        self.assertEqual(result,"Lipps_Asvph!")

