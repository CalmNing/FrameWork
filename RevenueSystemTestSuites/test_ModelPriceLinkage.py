#-*- coding:utf-8 -*-
#! /usr/bin/python
"""
    这里面这统一调用方法
    """



import unittest

from framework.browser_engine import BrowserEngine
from src.CrewsTakePricing_one import Pricing
from src.PriceLinkage import PriceLinkage

__author__ = 'Calm'


class test_ModelPriceLinkage(unittest.TestCase):
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
    # 城市价格数据同步
    def test_1(self):
        login = PriceLinkage(self.driver)
        # login = Pricing(self.driver)
        login.RevenueLogin()
        login.CarSetPricing()
        login.Synchronous_value()
        value = login.Mass_Effect()
        login.is_city_config(value)




if __name__ == '__main__':
    unittest.main()