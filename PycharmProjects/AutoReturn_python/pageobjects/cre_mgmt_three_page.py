#  -*- coding: utf-8 -*-

import re
from framework.basepage import BasePage
from framework.constans import Constans


class CreMgmtThreePage(BasePage):

    # def __init__(self,driver):
    #     super(CreMgmtThreePage, self).__init__(driver)
    #     self.total_price = None
    total_price = None

    # 车型组升级
    def close_the_update_frame(self, flag):
        self.sleep(3)
        if self.is_element_exsit(Constans.UPGRADE_ELEMENT):
            s = self.element_text(Constans.UPGRADE_ELEMENT).split('免费')[1].split("（钻石卡用户专享）")[0]
            if s == "车型组升级":
                if flag:
                    self.click(Constans.ONE_UPGRADE)
                    self.click(Constans.CLICK_OK_TO_UPGRADE)
                else:
                    self.click(Constans.CLOSE_THE_POPUP)
        else:
            print("该车型（车组）没有车型组升级")

    # 优惠活动
    def promotions(self):
        if self.is_element_exsit(Constans.PROMOTION_TEXT):
            self.click(Constans.PROMOTION_TEXT)
        i = 0
        while self.is_element_exsit(Constans.PROMOTION_SELECT) == False and i < 3:
            i += 1
        if i != 3:
            self.click(Constans.PROMOTION_SELECT)
            print(f"已使用优惠券！{self.element_text(Constans.PROMOTION_SELECT)}")
        else:
            print("未找到优惠券")

    # 选择增值服务
    def add_server(self, flag1, flag2):
        if flag1:
            self.click(Constans.DESIGNATED_MODEL)
            self.sleep(2)
            if self.is_element_exsit(Constans.DESIGNATED_MODEL_VAL):
                self.click(Constans.DESIGNATED_MODEL_VAL)
            else:
                print("该车型没有多余的库存")
        self.sleep(2)
        self.click(Constans.BASIS_MODEL)                                                     # 开始都为基础补充保障
        self.sleep(2)
        if flag2:
            self.click(Constans.AIRPORT_PICKUP)
        self.sleep(2)
        self.click(Constans.NO_OIL)
        self.sleep(2)

        # self.click(Constans.DELAYED_RETURN)
        # self.sleep(2)

    # 获取订单明细
    def charge_details(self):
        shop_time = self.element_text(Constans.SHOP_TIME1)                                   # 获取门店信息
        car_rental_fees1 = self.element_text(Constans.CAR_RENTAL_FEES1)                      # 车辆租赁费及门店服务费
        q = self.element_text(Constans.BASE_SECURITY_FEES1).split('\n')[1].split("\n")[0]
        if q == "基本保障服务费":
            base_security_fees1 = self.element_text(Constans.BASE_SECURITY_FEES1_VAL1)
        else:
            base_security_fees1 = self.element_text(Constans.BASE_SECURITY_FEES1_VAL2)
        other_server_fees1 = self.element_text(Constans.OTHER_SERVER_FEES1)                    # 其他服务费
        print("-----")
        # if self.is_element_exsit(Constans.DISCOUNT_FEES1):
        #     print("cunzai")
        w = self.element_text(Constans.DISCOUNT_FEES1).split('\n')[1].split("折扣")[0]
        if w == "优惠":
            discount_fees1 = self.element_text(Constans.DISCOUNT_FEES1_VAL1)
        else:
            discount_fees1 = "0"
        total_price1 = self.element_text(Constans.TOTAL_PRICE1).replace('\n', '')              # 总价

        print("********************  订单详情页，确定信息(mgmt创建订单)：********************")
        print("门店日期时间信息：%s" % shop_time)
        print("-----------------------        价格明细:          --------------------------")
        print("车辆租赁费及门店服务费：%s" % car_rental_fees1)
        print("基本保险费: %s" % base_security_fees1)
        print("其他服务费：%s" % other_server_fees1)
        print("优惠折扣: %s" % discount_fees1)
        print("总费用：%s" % total_price1)
        car_rental_fees = re.sub("\D", "", car_rental_fees1)
        base_security_fees = re.sub("\D", "", base_security_fees1)
        other_server_fees = re.sub("\D", "", other_server_fees1)
        discount_fees = re.sub("\D", "", discount_fees1)
        self.sleep(1)
        CreMgmtThreePage.total_price = re.sub("\D", "", total_price1)
        print(car_rental_fees, base_security_fees, other_server_fees, discount_fees)
        self.sleep(1)
        print(CreMgmtThreePage.total_price)

        total_price_add = float(car_rental_fees) + float(base_security_fees) + float(other_server_fees) - float(discount_fees)
        total_price_show = float(CreMgmtThreePage.total_price)
        print("计算的总价：%s  显示的总价：%s" % (total_price_add, total_price_show))
        if total_price_add == total_price_show:
            print("价格总价计算正确！")
        else:
            print("···请注意，价格计算不正确！···")
        self.click(Constans.UP)
        self.click(Constans.CRE_SUBMIT_ORDERS)
