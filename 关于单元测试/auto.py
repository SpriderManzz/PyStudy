# -*- coding: utf-8 -*-
from widget import Widget
import unittest
# 执行测试的类
class WeigetTestCse(unittest.TestCase):
        def setUp(self):
            self.widget = Widget()

        def testSize(self):
            self.assertEqual(self.widget.getSize(), (40, 60))

        def tearDown(self):
            self.widget =None

# 构造测试集
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WeigetTestCse("TestSize"))
    return suite

# 测试
if __name__ == "_main_":
    unittest.main(defaultTest='suite')
