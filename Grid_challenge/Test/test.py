import unittest
from Grid_challenge.Function.grid import gridChallenge ,all
from Grid_challenge.Test.test_plan import (
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
    list_14_question, list_14_ans
)

class TestDataTestCases(unittest.TestCase):

    def test_list_1(self):
        user_lst = list_1_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_1_ans)

    def test_list_3(self):
        user_lst = list_2_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_2_ans)

    def test_list_5(self):
        user_lst = list_3_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_3_ans)

    def test_list_3_2(self):
        user_lst = list_4_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_4_ans)

    def test_list_2(self):
        user_lst = list_5_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_5_ans)

    def test_list_4(self):
        user_lst = list_6_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_6_ans)

    def test_list_6(self):
        user_lst = list_7_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_7_ans)

    def test_list_4_2(self):
        user_lst = list_8_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_8_ans)

    def test_list_20(self):
        user_lst = list_9_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_9_ans)

    def test_list_11(self):
        user_lst = list_10_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_10_ans)

    def test_list_6_2(self):
        user_lst = list_11_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_11_ans)

    def test_list_2_2(self):
        user_lst = list_12_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_12_ans)

    def test_list_3_3(self):
        user_lst = list_13_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_13_ans)

    def test_list_100(self):
        user_lst = list_14_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_14_ans)