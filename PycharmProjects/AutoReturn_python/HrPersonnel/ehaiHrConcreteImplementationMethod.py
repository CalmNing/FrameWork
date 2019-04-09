#-*- coding:utf-8 -*-
#! /usr/bin/python
from PagePath.CrewsTakePricingPath import ehaihr_xpath
from framework.basepage import BasePage
import unittest


__author__ = 'Calm'

"""

人事系统的具体实现方法
"""

class ehaiHrConcreteImplementationMethod(BasePage):

    # ehi 家园的登录方法

    def ehi_login(self):
        self.input(ehaihr_xpath.Code_id,'11968')
        self.input(ehaihr_xpath.PassWord,'123456')
        self.click(ehaihr_xpath.LoginButton_id)
    def frame_title(self):
        return self.get_frame_title(ehaihr_xpath.IFRAME_id)
    def access_bx(self):
        print(self.get_frame_title(ehaihr_xpath.IFRAME_id))
        self.goto_iframe(ehaihr_xpath.IFRAME_id)
        self.click(ehaihr_xpath.BXID)
        self.sleep(5)
        # print(self.get_frame_title(ehaihr_xpath.IFRAME_id))

        return self.get_frame_title(ehaihr_xpath.IFRAME_id)







