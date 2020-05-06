import unittest
from autotest.testcase import *
# from autotest.testcase_temp_1.TestCase000 import *
# import autotest.testcase_temp_1

#创建测试套件实例
suite=unittest.TestSuite()
#添加测试用例1
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestCasetest))


#添加测试用例2
case1 = TestCasetest("test_addtempsensor")
suite.addTest(case1)

#运行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)