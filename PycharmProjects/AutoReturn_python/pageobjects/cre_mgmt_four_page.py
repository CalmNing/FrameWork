#  -*- coding: utf-8 -*-

from framework.basepage import BasePage
from framework.constans import Constans


class CreMgmtFourPage(BasePage):

    # def __init__(self, driver):
    #     super(CreMgmtFourPage, self).__init__(driver)
    #     self.order_number = None
    order_number = None

    def get_order_number(self):
        self.sleep(1)
        # self.alert_is_present()

        CreMgmtFourPage.order_number = self.element_text(Constans.GET_ORDER_NUMBER)
        # print(CreMgmtFourPage.order_number)
        self.click(Constans.CLICK_JUMP)

    def click_login(self):
        self.sleep(1)
        self.click(Constans.MY_YI_HAI_CLICK)

    def cookie(self):
        c = {'name': 'zjfr_fl', 'value': 'mdl', 'path': '/'}
        self.driver.add_cookie(c)

    def booking_login(self, name, password, text):
        self.click(Constans.MY_LOGIN_PT)
        self.type(Constans.MY_LOGIN_NAME, name)
        self.type(Constans.MY_LOGIN_PASSWORD, password)
        self.type(Constans.MY_LOGIN_PIC, text)
        self.sleep(1)
        self.click(Constans.CLICK_ON)