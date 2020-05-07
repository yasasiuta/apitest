import unittest
from autotest.testcase import TestCasetest
# from autotest.testcase_temp_1.TestCase000 import *
# import autotest.testcase_temp_1



#创建测试套件实例
suite=unittest.TestSuite()
#添加测试用例
suite.addTest(TestCasetest('test_1_addtempsensor'))
suite.addTest(TestCasetest('test_3_darutempsensor'))
# suite.addTest('test_2_delatetempsensor')
#运行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)