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
    def test_list_1(self):
        user_lst = list_1_question
        if isinstance(user_lst, list):
            result = all(user_lst)
        self.assertListEqual(result, list_1_ans)
        

        # list_1, list_2 = funnyString(list_1_question)
        # result = list_check(list_1, list_2)
        # self.assertListEqual(result, list_1_ans)

    # def test_list_2(self):
    #     list_1, list_2 = funnyString(list_2_question)
    #     result = list_check(list_1, list_2)
    #     self.assertListEqual(result, list_2_ans)

    # def test_list_3(self):
    #     list_1, list_2 = funnyString(list_3_question)
    #     result = list_check(list_1, list_2)
    #     self.assertListEqual(result, list_3_ans)

    # def test_list_4(self):
    #     list_1, list_2 = funnyString(list_4_question)
    #     result = list_check(list_1, list_2)
    #     self.assertListEqual(result, list_4_ans)

    # def test_list_5(self):
    #     list_1, list_2 = funnyString(list_5_question)
    #     result = list_check(list_1, list_2)
    #     self.assertListEqual(result, list_5_ans)

    # def test_list_6(self):
    #     list_1, list_2 = funnyString(list_6_question)
    #     result = list_check(list_1, list_2)
    #     self.assertListEqual(result, list_6_ans)
    
    # def test_list_7(self):
    #     list_1, list_2 = funnyString(list_7_question)
    #     result = list_check(list_1, list_2)
    #     self.assertListEqual(result, list_7_ans)

    # def test_list_8(self):
    #     list_1, list_2 = funnyString(list_8_question)
    #     result = list_check(list_1, list_2)
    #     self.assertListEqual(result, list_8_ans)

    # def test_list_9(self):
    #     list_1, list_2 = funnyString(list_9_question)
    #     result = list_check(list_1, list_2)
    #     self.assertListEqual(result, list_9_ans)

    # def test_list_10(self):
    #     list_1, list_2 = funnyString(list_10_question)
    #     result = list_check(list_1, list_2)
    #     self.assertListEqual(result, list_10_ans)

    # def test_list_11(self):
    #     list_1, list_2 = funnyString(list_11_question)
    #     result = list_check(list_1, list_2)
    #     self.assertListEqual(result, list_11_ans)