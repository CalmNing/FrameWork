#  -*- coding: utf-8 -*-

from framework.basepage import BasePage
from framework.constans import Constans


class ModMgmtTwoPage(BasePage):

    def choose_place(self, csi, csv, ssi, ssv, cei, cev, sei, sev):
        self.handle()
        self.sleep(2)
        self.set_js_value(Constans.PICK_UP_THE_CITY, csi)
        self.set_js_value(Constans.PICK_UP_THE_CITY_ID, csv)
        self.set_js_value(Constans.PICK_UP_THE_SHOP, ssi)
        self.set_js_value(Constans.PICK_UP_THE_SHOP_ID, ssv)
        self.set_js_value(Constans.RETURN_THE_CITY, cei)
        self.set_js_value(Constans.RETURN_THE_CITY_ID, cev)
        self.set_js_value(Constans.RETURN_THE_SHOP, sei)
        self.set_js_value(Constans.RETURN_THE_SHOP_ID, sev)

    # 选择送车上门和上门取车
    def choose_home_place(self, csi, csv, cei, cev):
        self.handle()
        self.sleep(4)
        self.set_js_value(Constans.PICK_UP_THE_CITY, csi)
        self.set_js_value(Constans.PICK_UP_THE_CITY_ID, csv)
        self.click(Constans.DELIVERY_TO_THE_DOOR)
        self.click(Constans.TWO_TOLL)
        self.click(Constans.TWO_TOLL_CLICK)
        self.alert_is_present()
        self.sleep(1)
        self.set_js_value(Constans.RETURN_THE_CITY, cei)
        self.set_js_value(Constans.RETURN_THE_CITY_ID, cev)
        self.click(Constans.PICK_UP_THE_CAR)
        self.click(Constans.FOUR_TOLL)
        self.click(Constans.FOUR_TOLL_CLICK)
        self.alert_is_present()

    # 选择时间（用js改属性值，节约时间）
    def choose_time(self, date_start, tsi, tsv, date_end, tei, tev):
        js1 = "document.getElementById('J_date_1').removeAttribute('readonly')"
        self.driver.execute_script(js1)
        js2 = "document.getElementById('J_date_2').removeAttribute('readonly')"
        self.driver.execute_script(js2)
        self.type("J_date_1", date_start)
        self.set_js_value(Constans.PICK_UP_TIME_ID, tsi)
        self.set_js_value(Constans.PICK_UP_TIME_VALUE, tsv)
        self.click(Constans.RETURN_SHOP_TEXT)
        self.type("J_date_2", date_end)
        self.set_js_value(Constans.RETURN_TIME_ID, tei)
        self.set_js_value(Constans.RETURN_TIME_VALUE, tev)
        self.click(Constans.RETURN_SHOP_TEXT)

    # 点击重算价格
    def recalculate_price(self):
        self.click(Constans.RECALCULATE_PRICE)

    # 点击下一步（挑选车型）
    def pick_model(self):
        self.handle()
        self.sleep(2)
        self.click(Constans.PICK_MODEL)