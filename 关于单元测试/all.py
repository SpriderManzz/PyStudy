# -*- coding: utf-8 -*-
from widget import Widget
import unittest
# 执行测试的类
class WidgetTestCse(unittest.TestCase):
        def setUp(self):
            self.widget = Widget()

        def testSize(self):
            self.assertEqual(self.widget.getSize(), (40, 60))

        def testResize(self):
            self.widget.rease(100.100)
            self.assertEqual(self.widget.getSize(), (100, 60))

        def tearDown(self):
            self.widget.dispose()
            self.widget = None




# 测试
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCse("testSize"))
    suite.addTest(WidgetTestCse("testResize"))

# 执行测试
runner = unittest.TextTestRunner()
runner.run(suite)
