# coding=utf-8
from survey import AnonymousSurvey
import unittest

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "你第一门的学习语言是什么?" # 把它变成属性
        self.my_survey = AnonymousSurvey(question)  # 根据这个问题来创建了一个实例
        self.languages =['国语' , '客家', '粤语']

    def test_single_store_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.languages[0])  # 传值调用AnonymousSurvey类的方法store_respons
        self.assertIn(self.my_survey.responses[0], self.languages)

    def test_three_store_response(self):
        for i in self.languages:
            self.my_survey.store_response(i)
        for i in self.languages:
            self.assertIn(i,self.my_survey.responses)

unittest.main()