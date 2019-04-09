#-*- coding:utf-8 -*-
#! /usr/bin/python
from HrPersonnel.ehaiHrConcreteImplementationMethod import ehaiHrConcreteImplementationMethod

__author__ = 'Calm'


import unittest

from framework.browser_engine import BrowserEngine
from src.CrewsTakePricing_one import Pricing

__author__ = 'Calm'


class CrewsTakePricing(unittest.TestCase):

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

    def test_Case_ehi(self):
        ehiHr = ehaiHrConcreteImplementationMethod(self.driver)
        ehiHr.ehi_login()
        # ehiHr.frame_title()

        print(ehiHr.access_bx())
        print("#####################")
        ehiHr.sleep(5)
        self.assertIn("一嗨财务报销",ehiHr.access_bx(),msg="一嗨财务报销不在当前页面title中，测试未通过")

if __name__ == '__main__':
    unittest.main()
