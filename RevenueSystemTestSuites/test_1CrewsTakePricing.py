#-*- coding:utf-8 -*-
#! /usr/bin/python
"""
    这里面这统一调用方法
    """



import unittest

from framework.browser_engine import BrowserEngine
from src.CrewsTakePricing_one import Pricing

__author__ = 'Calm'


class test_CrewsTakePricing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
                测试固件的setUp()的代码，主要是测试的前提准备工作
                :return:
                """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        print(cls.driver)



    @classmethod

    def tearDown(cls):
        """
                测试结束后的操作，这里基本上都是关闭浏览器
                :return:
                """
        cls.driver.quit()
    # 更新同城
    def test_2(self):
        login = Pricing(self.driver)
        # print(login.RevenueLogin())
        login.RevenueLogin()

        login.CarSetPricing_one()
        login.Synchronous_value()
        login.Mass_Effect()
        login.updateCity()



if __name__ == '__main__':
    unittest.main()