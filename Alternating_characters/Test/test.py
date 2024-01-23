import unittest
from Alternating_characters.Function.alternative_char import alternatingCharacters , all
from Alternating_characters.Test.test_case import (
    list_1_question, list_1_ans,
    list_2_question, list_2_ans,
    list_3_question, list_3_ans,
    list_4_question, list_4_ans,
    list_5_question, list_5_ans,
    list_6_question, list_6_ans,
    list_7_question, list_7_ans,
    list_8_question, list_8_ans,
    list_9_question, list_9_ans,
    list_10_question, list_10_ans,
    list_11_question, list_11_ans,
    list_12_question, list_12_ans,
    list_13_question, list_13_ans,
    list_14_question, list_14_ans,
    list_15_question, list_15_ans
)

class TestDataTestCases(unittest.TestCase):
    def test_list_8 (self) :
        user_lst = list_1_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_1_ans)
    
    def test_list_4999_3265_1212_2005 (self) :
        user_lst = list_2_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_2_ans)

    def test_list_5596_7826 (self) :
        user_lst = list_3_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_3_ans)

    def test_list_4_5_8_6_6 (self) :
        user_lst = list_4_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_4_ans)
    
    def test_list_10_8_8 (self) :
        user_lst = list_5_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_5_ans)

    def test_list_123_456_789_147_258_369_741_852_963 (self) :
        user_lst = list_6_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_6_ans)
    
    def test_list_1266_1580_1477_1172_1098_1691_1071_1440 (self) :
        user_lst = list_7_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_7_ans)
    
    def test_list_9_16_4_8_15_7 (self) :
        user_lst = list_8_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_8_ans)

    def test_list_34_29_30_33_26_24_20 (self) :
        user_lst = list_9_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_9_ans)

    def test_list_73_99_95_88_66_48_81_91_51_64 (self) :
        user_lst = list_10_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_10_ans)
    
    def test_list_128_190 (self) :
        user_lst = list_11_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_11_ans)

    def test_list_251_464_299_294_330_331_305_249_228 (self) :
        user_lst = list_12_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_12_ans)

    def test_list_539_526_647_685_654_515_710_772_732_746 (self) :
        user_lst = list_13_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_13_ans)
    
    def test_list_2_41_65_45_88 (self) :
        user_lst = list_14_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_14_ans)

    def test_list_1518_2187_2283 (self) :
        user_lst = list_15_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_15_ans)
