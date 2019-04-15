# -*- coding: utf-8 -*-

import re
from framework.basepage import BasePage
from framework.constans import Constans


class ModBookingYihaiPage(BasePage):

    # def __init__(self, driver):
    #     super(ModBookingYihaiPage, self).__init__(driver)
    #     self.total_price = None
    total_price = None

    def my_order(self, flag):
        self.click(Constans.MY_YI_HAI_CLICK)
        self.click(Constans.CHOOSE_LOGIN_TYPE)
        self.click(Constans.CLICK_ORDER_MANAGE)
        self.click(Constans.GET_BEFORE_MONEY)
        self.sleep(1)
        shop_time = self.element_text(Constans.SHOP_TIME2)
        car_rental_fees2 = self.element_text(Constans.CAR_RENTAL_FEES2)
        q = self.element_text(Constans.BASE_SECURITY_FEES2).split('服务费')[0]
        if q == "基本保障":
            base_security_fees2 = self.element_text(Constans.BASE_SECURITY_FEES2_VAL1)
        else:
            base_security_fees2 = self.element_text(Constans.BASE_SECURITY_FEES2_VAL2)
        other_server_fees2 = self.element_text(Constans.OTHER_SERVER_FEES2)
        w = self.element_text(Constans.DISCOUNT_FEES2).replace('折扣', '')
        if w == "优惠":
            discount_fees2 = self.element_text(Constans.DISCOUNT_FEES2_VAL1)
        else:
            discount_fees2 = "0"
        total_price2 = self.element_text(Constans.TOTAL_PRICE2).replace('\n', '')

        print("********************  订单详情页，确定信息(booking核对修改后的订单)：********************")
        print("门店日期时间信息：%s" % shop_time)
        print("-----------------------        价格明细:          --------------------------")
        print("车辆租赁费及门店服务费：%s" % car_rental_fees2)
        print("基本保险费: %s" % base_security_fees2)
        print("其他服务费：%s" % other_server_fees2)
        print("优惠折扣: %s" % discount_fees2)
        print("总费用：%s" % total_price2)
        car_rental_fees = re.sub("\D", "", car_rental_fees2)
        base_security_fees = re.sub("\D", "", base_security_fees2)
        other_server_fees = re.sub("\D", "", other_server_fees2)
        discount_fees = re.sub("\D", "", discount_fees2)
        ModBookingYihaiPage.total_price = re.sub("\D", "", total_price2)
        print(car_rental_fees, base_security_fees, other_server_fees, discount_fees)
        print(ModBookingYihaiPage.total_price)
        total_price_add = float(car_rental_fees) + float(base_security_fees) + float(other_server_fees) - float(discount_fees)
        total_price_show = float(ModBookingYihaiPage.total_price)
        print("计算的总价：%s  显示的总价：%s" % (total_price_add, total_price_show))
        if total_price_add == total_price_show:
            print("价格总价计算正确！")
        else:
            print("···请注意，价格计算不正确！···")
        if flag:
            self.click(Constans.CLICK_CANCEL_ORDER)
            self.click(Constans.CANCEL_REASON)
            self.click(Constans.CANCEL)
            self.alert_is_present()

    # 关闭页面
    def shut_down(self):
        self.quit_browser()


