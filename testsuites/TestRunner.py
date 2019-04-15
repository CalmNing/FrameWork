# coding = utf-8
import unittest
import HTMLTestRunner
# 声明测试用例的路径
test_dir="D:\\PycharmProjects\\AutoReturn_python\\testsuites"

discover = unittest.TestLoader().discover(test_dir,pattern='test*.py',top_level_dir= None)

if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    # fp = file(filename, 'wb')
    # # 定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'百度搜索测试报告', description=u'用例执行情况：')
    # # 运行测试用例
    runner.run(discover)
    # fp.close()



