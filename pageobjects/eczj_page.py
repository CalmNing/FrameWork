#  -*- coding: utf-8 -*-

from framework.basepage import BasePage


class EczjPage(BasePage):

    USER_NAME = "id=>username"
    USER_PASSWORD = "id=>password"
    LOGIN_IN = "id=>btnSubmit"
    ORDER_PROCESS_CENTER = "id=>ctl00_ContentPlaceHolder1_dlMenu_ctl00_dlChildMenu_ctl00_lnkChildMenu"
    ORDER_NUMBER = "id=>ctl00_ContentPlaceHolder1_txtOrderNo"
    CLICK_SEARCH = "id=>ctl00_ContentPlaceHolder1_btnSearch"
    MODIFY_ORDER = "id=>ctl00_ContentPlaceHolder1_rgOrder_ctl02_lnkEditOrder"

    def eczj_link(self):
        self.link("http://eczj.1hai.cn")

    def eczj_login(self):
        self.type(self.USER_NAME, "11968")
        self.type(self.USER_PASSWORD, "123456")
        self.click("id=>btnSubmit")

    def eczj_create_order(self):
        self.click("id=>ctl00_ContentPlaceHolder1_dlMenu_ctl00_dlChildMenu_ctl01_lnkChildMenu")
        self.click("id=>ctl00_ContentPlaceHolder1_rbtOrder")
        self.type("id=>ctl00_ContentPlaceHolder1_txtPhone", "15731678287")
        self.click("id=>ctl00_ContentPlaceHolder1_btnSearch")
        self.click("id=>ctl00_ContentPlaceHolder1_grdUserInfo_ctl03_lnkChoose")

    def eczj_order_center(self, text):
        self.click(self.ORDER_PROCESS_CENTER)
        self.input(self.ORDER_NUMBER, text)
        self.click(self.CLICK_SEARCH)
        self.click(self.MODIFY_ORDER)








