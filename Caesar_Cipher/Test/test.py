from Caesar_Cipher.Function.caesar_cipher import get_caesarCipher
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_Lipps_Asvph (self): 
        n = 12
        s = 'Hello_World'
        k = 4
        result = get_caesarCipher(s, k)
        self.assertEqual(result,"Lipps_Asvph")
    
    def test_give_Ciphering (self): 
        n = 10
        s = 'Ciphering'
        k = 26
        result = get_caesarCipher(s, k)
        self.assertEqual(result,"Ciphering")
    
    def test_give_fff_jkl_gh (self): #fff.jkl.gh
        n = 10
        s = 'www.abc.xy'
        k = 87
        result = get_caesarCipher(s, k)
        self.assertEqual(result,"fff.jkl.gh")

    def test_give_159357fwzx (self): 
        n = 10
        s = '159357lcfd'
        k = 98
        result = get_caesarCipher(s, k)
        self.assertEqual(result,"159357fwzx")

    def test_give_D3q4 (self): 
        n = 4
        s = 'D3q4'
        k = 0
        result = get_caesarCipher(s, k)
        self.assertEqual(result,"D3q4")

    def test_give_okffng_Qwvb (self): #okffng-Qwvb
        n = 11
        s = 'middle-Outz'
        k = 2
        result = get_caesarCipher(s, k)
        self.assertEqual(result,"okffng-Qwvb")

    def test_give_90_string (self): #!w-bL`-yX!.G`mVKmFlX/MaCyyvSS!CSwts.!g/`He`eJk1DGZBa`eBLdyu`hZD`vV-jZDm.LCBSre..-!.!dmv!-E
        n = 90
        s = '!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U'
        k = 62
        result = get_caesarCipher(s, k)
        self.assertEqual(result,"!w-bL`-yX!.G`mVKmFlX/MaCyyvSS!CSwts.!g/`He`eJk1DGZBa`eBLdyu`hZD`vV-jZDm.LCBSre..-!.!dmv!-E")




