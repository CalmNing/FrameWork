#-*- coding:utf-8 -*-
#! /usr/bin/python
import time

__author__ = 'Calm'
import unittest
import HTMLTestRunner
import HTMLTestRunnerCN
# 声明测试用例的路径
test_dir="D:\\PycharmProjects\\AutoReturn_python\\RevenueSystemTestSuites"

discover = unittest.TestLoader().discover(test_dir, pattern='test_*.py', top_level_dir= None)

# print(discover)




if __name__ == '__main__':
    now = time.strftime("%Y%m%d-%H:%M:%S", time.localtime(time.time()))
    filePath = 'D:\\Report\\' + now + 'Report.html'

    # 确定生成报告的路径
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title='收益系统测试报告',
        # description='详细测试用例结果',
        tester='QA'
    )
    # 运行测试用例
    runner.run(discover)
    # 关闭文件，否则会无法生成文件
    fp.close()
