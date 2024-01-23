import unittest
from Funny_String.Function.funny_or_not import funnyString ,list_check ,all
from Funny_String.Test.list_case import (
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
    list_11_question, list_11_ans
)

class TestDataTestCases(unittest.TestCase):

    def test_list_4_4(self):
        user_lst = list_1_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_1_ans)

    def test_list_6_5(self):
        user_lst = list_2_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_2_ans)

    def test_list_36_5_18_54_98_27_20_33_77_11(self):
        user_lst = list_3_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_3_ans)

    def test_list_99_9_10(self):
        user_lst = list_4_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_4_ans)

    def test_list_2359_79_12_777(self):
        user_lst = list_5_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_5_ans)

    def test_list_956_70_12_1046_17(self):
        user_lst = list_6_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_6_ans)
    
    def test_list_26(self):
        user_lst = list_7_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_7_ans)

    def test_list_91_2_7455_2025_12_6500(self):
        user_lst = list_8_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_8_ans)

    def test_list_2_70_206_12_4545_5555_12_936_2525(self):
        user_lst = list_9_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_9_ans)

    def test_list_4343_945_7_435_9_9_9(self):
        user_lst = list_10_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_10_ans)

    def test_list_476_9_741_852_5_123_7_789(self):
        user_lst = list_11_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_11_ans)