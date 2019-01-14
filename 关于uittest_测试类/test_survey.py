# coding=utf-8
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurver(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def test_single_store_response(self):
        """测试单个答案会被妥善地存储"""
        question = "你第一门的学习语言是什么?"
        my_survey_single = AnonymousSurvey(question)   # 根据这个问题来创建了一个实例
        my_survey_single.store_response('国语')
        self.assertIn('国语',my_survey_single.responses)

    def test_three_store_response(self):
        """测试3个答案是否也会被妥善地存储"""
        question = "你第一门的学习语言是什么?"
        my_survey_three = AnonymousSurvey(question)  # 根据这个问题来创建了一个实例
        languages =['国语' , '客家', '粤语']
        for i in languages:
            my_survey_three.store_response(i)
        for i in languages:
            self.assertIn(i, my_survey_three.responses)

unittest.main()