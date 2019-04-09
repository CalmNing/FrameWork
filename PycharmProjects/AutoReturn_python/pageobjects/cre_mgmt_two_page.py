#  -*- coding: utf-8 -*-

from framework.basepage import BasePage
from framework.constans import Constans
from selenium.webdriver import ActionChains


class CreMgmtTwoPage(BasePage):

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
        self.sleep(3)
        self.set_js_value(Constans.PICK_UP_THE_CITY, csi)
        self.set_js_value(Constans.PICK_UP_THE_CITY_ID, csv)
        self.click(Constans.DELIVERY_TO_THE_DOOR)
        self.click(Constans.TWO_TOLL)
        self.click(Constans.TWO_TOLL_CLICK)
        self.alert_is_present()
        self.set_js_value(Constans.RETURN_THE_CITY, cei)
        self.set_js_value(Constans.RETURN_THE_CITY_ID, cev)
        self.click(Constans.PICK_UP_THE_CAR)
        self.click(Constans.FOUR_TOLL)
        self.click(Constans.FOUR_TOLL_CLICK)
        self.alert_is_present()

    # 选择时间（用js改属性值，节约时间）
    def choose_time(self, date_start, tsi, tsv, date_end, tei, tev):
        self.sleep(3)
        js1 = "document.getElementById('J_date_1').removeAttribute('readonly')"
        self.driver.execute_script(js1)
        js2 = "document.getElementById('J_date_2').removeAttribute('readonly')"
        self.driver.execute_script(js2)
        self.type("J_date_1", date_start)
        self.set_js_value(Constans.PICK_UP_TIME_ID, tsi)
        self.set_js_value(Constans.PICK_UP_TIME_VALUE, tsv)
        self.click(Constans.PICK_UP_SHOP)
        self.type("J_date_2", date_end)
        self.set_js_value(Constans.RETURN_TIME_ID, tei)
        self.set_js_value(Constans.RETURN_TIME_VALUE, tev)
        self.click(Constans.BTN_SUBMIT)

    # 选择的支付类型，自定义switch方法，节约时间
    def switch(self, choose):
        self.sleep(2)
        pay = '支付方式'
        if self.is_element_exsit(Constans.FLASH_RENT):
            element = self.find_element(Constans.GET_MOVE_ELEMENT)
            ActionChains(self.driver).move_to_element(element).perform()
            for case in Switch(choose):
                if case(0):
                    pay = self.find_element(Constans.FLASH_RENTAL_PRICE).text
                    self.click(Constans.FLASH_RENTAL_PRICE)
                    break
                if case(1):
                    pay = self.find_element(Constans.PAY_AT_THE_STORE1).text
                    self.click(Constans.PAY_AT_THE_STORE1)
                    break
                if case(2):
                    pay = self.find_element(Constans.RETURN_PRICE1).text
                    self.click(Constans.RETURN_PRICE1)
                    break
                if case(3):
                    pay = self.find_element(Constans.PACKAGE_PRICE1).text
                    self.click(Constans.PACKAGE_PRICE1)
            print("选择支付的方式为: %s" % pay)
        else:
            for case in Switch(choose):
                element = self.find_element(Constans.GET_MOVE_ELEMENT)
                ActionChains(self.driver).move_to_element(element).perform()
                if case(1):
                    pay = self.find_element(Constans.PAY_AT_THE_STORE2).text
                    self.click(Constans.PAY_AT_THE_STORE2)
                    break
                if case(2):
                    pay = self.find_element(Constans.RETURN_PRICE2).text
                    self.click(Constans.RETURN_PRICE2)
                    break
                if case(3):
                    pay = self.find_element(Constans.PACKAGE_PRICE2).text
                    self.click(Constans.PACKAGE_PRICE2)
                    break
            print("选择支付的方式为: %s" % pay)


class Switch(object):

    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

'''
    # 门店选择
    def choose_place1(self):
        handles = self.driver.window_handles  # 获取当前全部窗口句柄集合
        print(handles)
        for handle in handles:  # 切换窗口
            if handle != self.driver.current_window_handle:
                print('switch to second window', handle)
                self.close()  # 关闭第一个窗口
            self.driver.switch_to.window(handle)  # 切换到第二个窗口

        self.clicks_input(Constans.PICK_UP_THE_CITY, Constans.DETERMINE_THE_CITY, "上海")
        self.clicks_input(Constans.PICK_UP_THE_SHOP, Constans.DETERMINE_THE_SHOP, Constans.SHOP_START)
        self.clicks_input(Constans.RETURN_CITY, Constans.DETERMINE_THE_CITY, "上海")
        self.clicks_input(Constans.RETURN_THE_SHOP, Constans.DETERMINE_THE_RETURN_SHOP, Constans.SHOP_END)
        self.sleep(3)

    # 时间选择
    def choose_time1(self, date_start, date_end, time_start, time_end):
        js1 = "document.getElementById('J_date_1').removeAttribute('readonly')"
        self.driver.execute_script(js1)
        js2 = "document.getElementById('J_date_2').removeAttribute('readonly')"
        self.driver.execute_script(js2)
        js3 = "document.getElementById('getHour').removeAttribute('readonly')"
        self.driver.execute_script(js3)
        js4 = "document.getElementById('retHour').removeAttribute('readonly')"
        self.driver.execute_script(js4)
        self.type("J_date_1", date_start)
        self.type("getHour", time_start)
        self.click(Constans.RETURN_CAI_TIME)
        self.type("J_date_2", date_end)
        self.type("retHour", time_end)
        self.click(Constans.BTN_SUBMIT)

    # 选择支付类型(不建议用)
    def price_type(self, choose):
        self.sleep(1)
        pay = '支付方式'
        if self.is_element_exsit(Constans.FLASH_RENT):
            element = self.find_element(Constans.GET_MOVE_ELEMENT)
            ActionChains(self.driver).move_to_element(element).perform()
            if choose == 0:
                pay = self.find_element(Constans.FLASH_RENTAL_PRICE).text
                self.click(Constans.FLASH_RENTAL_PRICE)
            elif choose == 1:
                pay = self.find_element(Constans.PAY_AT_THE_STORE1).text
                self.click(Constans.PAY_AT_THE_STORE1)
            elif choose == 2:
                pay = self.find_element(Constans.RETURN_PRICE1).text
                self.click(Constans.RETURN_PRICE1)
            elif choose == 3:
                pay = self.find_element(Constans.PACKAGE_PRICE1).text
                self.click(Constans.PACKAGE_PRICE1)
        else:
            self.sleep(1)
            element = self.find_element(Constans.GET_MOVE_ELEMENT)
            ActionChains(self.driver).move_to_element(element).perform()
            if choose == 1:
                pay = self.find_element(Constans.PAY_AT_THE_STORE2).text
                self.click(Constans.PAY_AT_THE_STORE2)
            elif choose == 2:
                pay = self.find_element(Constans.RETURN_PRICE2).text
                self.click(Constans.RETURN_PRICE2)
            elif choose == 3:
                pay = self.find_element(Constans.PACKAGE_PRICE2).text
                self.click(Constans.PACKAGE_PRICE2)
        print("选择支付的方式为: %s" % pay)
'''




    # #  悬停；抽取为公共方法，用参数去控制选取什么价格类型
    # time.sleep(2)
    # element = self.find_element_by_xpath("//*[@id=\"reservationList\"]/div[1]/ul/li[3]/p[1]/span[3]")
    # ActionChains(self).move_to_element(element).perform()
    # self.find_element_by_xpath("//*[@id=\"reservationList\"]/div[1]/ul/li[3]/p[1]/span[4]/a[2]").click()
    # # all_handles = self.window_handles
    # # print(all_handles)
    # self.find_element_by_xpath("//*[@id=\"mshowbox\"]/div/a").click()  # 关闭车型组升级，点击x号关闭
    #
    # # 各种优惠活动，抽取为公共的方法
    # # self.find_element_by_id("free").click().text.split("(")[1].split(")")[0]     # 使用免费天数
    # # self.find_element_by_id("PromotionCode").click()                             # 使用优惠编码
    # # self.find_element_by_xpath("//*[@id=\"3gTiqSkjR6w=\"]/div[2]").click()
    # # self.find_element_by_id("promotions").click()                                # 使用一嗨会员专享优惠
    # # self.find_element_by_id("lKKl4KT3I18=").click()
    # # self.find_element_by_id("channelpromotions").click()                        # 使用合作专享优惠
    # # self.find_element_by_xpath("//*[@id=\"wx9BrHcNFMk=\"]/img")
    # # self.find_element_by_id("999").click()                                        # 不参加优惠活动
    #
    # # 各种增值服务，抽取为公共的方法
    # # self.find_element_by_id("zdcx").click()  # 指定车型费
    # # self.find_element_by_id("231").click()   # 基础补充保障
    # # self.find_element_by_id("232").click()   # 高级补充保障
    # # self.find_element_by_id("233").click()   # 尊享补充保障
    # # self.find_element_by_id("209").click()   # 机场接机费
    # # self.find_element_by_id("234").click()   # 免加油服务费
    #
    # # 此时我需要获取价格类型  1、车辆租赁费及门店服务费  2、基本保障服务费  3、其他服务费  4、优惠折扣  5、总价
    # vehicle_store_fee = self.find_element_by_id("baseRatePrice").text.split('￥')[1].split("\n")[0]
    # basic_service_fee = self.find_element_by_xpath("//*[@id=\"priceall\"]/div/ul/li[2]/em").text.split('￥')[1]
    # other_service_fees = self.find_element_by_xpath("//*[@id=\"servicePriceList\"]/em").text.split('￥')[1]
    # # discount = self.find_element_by_xpath("//*[@id=\"promotionPriceList\"]/em").text.split('￥-')[1]
    # total_price = self.find_element_by_id("priceTotal").text.split('￥\n')[1]
    # print("车辆租赁费及门店服务费:%s  基本保障服务费:%s  其他服务费:%s   总价:%s" \
    #       % (vehicle_store_fee, basic_service_fee, other_service_fees, total_price))
    #
    # self.find_element_by_id("btnSubmit").click()  # 提交订单
    # time.sleep(3)
    # # 获取订单号
    # order_id = self.find_element_by_xpath("//*[@id=\"divOrderInfo\"]/span[1]").text
    # pay_price = self.find_element_by_xpath("//*[@id=\"divOrderInfo\"]/span[3]").text.split("￥")[1].split(".")[0]
    # print("%s  总价1：%s" % (order_id, pay_price))
    # self.find_element_by_xpath("//*[@id=\"wrap\"]/div[1]/div[2]/div/a").click()
    # time.sleep(3)
    # print("下单成功")
    # self.find_element_by_id("linkLogin").click()
    # time.sleep(3)
    # c = {'name': 'zjfr_fl', 'value': 'mdl', 'path': '/'}
    # self.add_cookie(c)
    # self.find_element_by_xpath("//*[@id=\"loginFrom\"]/div/div/div[1]/div[2]/label[2]/input").click()
    # self.find_element_by_id("txtLoginName").send_keys("13955665476")
    # self.find_element_by_id("txtPassword").send_keys("zhang19941206")
    # self.find_element_by_id("txtcaptcha").send_keys("9999")
    # self.find_element_by_id("ahrLogin").click()
    # time.sleep(3)
    # self.find_element_by_xpath("//*[@id=\"Form1\"]/div[3]/div[1]/div[1]/div/div[1]/a").click()
    # time.sleep(3)
    # self.find_element_by_xpath("//*[@id=\"content\"]/div/div[2]/dl/dd[1]/a").click()
    # self.find_element_by_xpath("//*[@id=\"content\"]/div/div[1]/div[2]/div[1]/ul/li[2]/a").click()
    # # js="var q=document.documentElement.scrollTop=10000"
    # # self.execute_script(js)
    # time.sleep(3)
    # self.find_element_by_xpath(
    #     '//*[@id="content"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]/a').click()
    # time.sleep(3)
    # self.find_element_by_id("btn-cancel").click()
    # self.find_element_by_xpath("//*[@id=\"cancelOrder\"]/div[2]/ul/li[1]/span").click()
    # time.sleep(3)
    # self.quit()