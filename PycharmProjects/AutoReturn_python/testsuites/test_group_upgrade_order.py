#  -*-coding: utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.eczj_page import EczjPage
from pageobjects.cre_mgmt_two_page import CreMgmtTwoPage
from pageobjects.cre_mgmt_three_page import CreMgmtThreePage
from pageobjects.cre_mgmt_four_page import CreMgmtFourPage
from pageobjects.cre_booking_yihai_page import CreBookingYihaiPage
from pageobjects.mod_mgmt_two_page import ModMgmtTwoPage
from pageobjects.mod_mgmt_three_page import ModMgmtThreePage
from pageobjects.mod_mgmt_four_page import ModMgmtFourPage
from pageobjects.mod_booking_yihai_page import ModBookingYihaiPage


class GroupOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_group_upgrade(self):
        """
        创建：同城市异门店（非机场店）—白天时间—门店现付价-车型组升级+（优惠）+增值服务
        修改：地图送还车门店（非机场店）-夜间时间（夜间取、还车费）-增值服务
        :return:
        """
        # 实例化对象，并入参驱动
        eczj_page = EczjPage(self.driver)
        # 调用 eczj_login 方法
        eczj_page.eczj_login()
        # 调用 eczj_create_order 方法
        eczj_page.eczj_create_order()

        # 实例化对象，并入参驱动
        cre_two_page = CreMgmtTwoPage(self.driver)
        cre_two_page.choose_place("上海", "77", "八万人体育场店", "886", "上海", "77", "张江店", "87")
        cre_two_page.choose_time("2019-02-15", "10时", "10", "2019-02-18", "10时", "10")
        cre_two_page.switch(1)                                                           # 选择门店现付价

        cre_three_page = CreMgmtThreePage(self.driver)
        cre_three_page.close_the_update_frame(True)
        cre_three_page.add_server(False, False)
        cre_three_page.charge_details()

        cre_four_page = CreMgmtFourPage(self.driver)
        cre_four_page.get_order_number()
        cre_four_page.click_login()
        cre_four_page.cookie()
        cre_four_page.booking_login("13955665476", "zhang19941206", "9999")

        cre_booking_page = CreBookingYihaiPage(self.driver)
        cre_booking_page.my_order()
        if CreMgmtThreePage.total_price == CreBookingYihaiPage.total_price:
            print(CreMgmtThreePage.total_price, CreBookingYihaiPage.total_price)
            print("创建时订单总价一致")
        else:
            print(CreMgmtThreePage.total_price, CreBookingYihaiPage.total_price)
            print("创建时订单总价不一致")

        eczj_page.eczj_link()
        eczj_page.eczj_login()
        eczj_page.eczj_order_center(CreMgmtFourPage.order_number)

        mod_two_page = ModMgmtTwoPage(self.driver)
        mod_two_page.choose_home_place("上海", "77", "上海", "77")
        mod_two_page.choose_time("2019-02-19", "12时", "12", "2019-02-22", "18时", "18")
        mod_two_page.recalculate_price()
        mod_two_page.pick_model()

        mod_three_page = ModMgmtThreePage(self.driver)
        mod_three_page.add_server(False, False)
        mod_three_page.charge_details()

        mod_four_page = ModMgmtFourPage(self.driver)
        mod_four_page.click_jump()

        mod_booking_page = ModBookingYihaiPage(self.driver)
        mod_booking_page.my_order(True)
        if mod_three_page.total_price == mod_booking_page.total_price:
            print("价格一样")
        else:
            print("价格不一样")


if __name__ == '__main__':
    unittest.main()




