# coding=utf-8
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function有没有被改出BUG"""
    def setUp(self):
        pass

    def test_first_last(self):
        """验证是否正确按name_function模块的要求正确输出名字"""
        formatted_name = get_formatted_name('tom', 'cat')
        self.assertEqual(formatted_name, 'Tomcat')

    def test_first_middle_last(self):
        """因为name_funtion改了代码"""
        formatted_name2 = get_formatted_name('tom', 'cat', 'join')
        self.assertEqual(formatted_name2, 'Tomjoincat')   #  一定要写成self

    def tearDown(self):
        pass

def suite():
    """中定义一个名为 suite()的全局函数"""
    suite = unittest.TestSuite()
    suite.addTest(NamesTestCase("test_first_last"))
    suite.addTest(NamesTestCase("test_first_middle_last"))
    return suite

if __name__ == "__main__":
    unittest.main()