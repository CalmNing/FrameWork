#-*- coding:utf-8 -*-
#! /usr/bin/python
import numpy as np
from selenium.webdriver.common.keys import Keys

from PagePath.CrewsTakePricingPath import RevenuePath
from framework.Time import Time
from framework.basepage import BasePage
# import unittest

__author__ = 'Calm'

"""
    这里面将实现具体的操作方法
    """

class Pricing(BasePage):
    global val_A
    val_A = np.random.randint(low=50, high=100)
    global val_B
    val_B = np.random.randint(low=20, high=50)


    # 登录收益系统
    def RevenueLogin(self):
        self.input(RevenuePath.CODE_ID, 11968)
        self.input(RevenuePath.PASSWORD_ID, 123456)
        self.click(RevenuePath.btnSubmit_ID)
        self.sleep(5)

        return self.get_page_title()

    # 车组调价查询
    def CarSetPricing(self):
        self.click(RevenuePath.GroupPriceXPATH)
        self.sleep(5)
        self.find_element(RevenuePath.CITYXPATH).send_keys(Keys.SPACE)
        self.sleep(1)
        self.input(RevenuePath.CITYXPATH, "上海")
        self.sleep(1)
        self.find_element(RevenuePath.CITYXPATH).send_keys(Keys.ENTER)
        self.clear(RevenuePath.STORESXPATH)
        self.find_element(RevenuePath.STORESXPATH).send_keys(Keys.SPACE)
        self.sleep(1)
        self.input(RevenuePath.STORESXPATH, "八万人体育场店")
        self.sleep(1)
        self.find_element(RevenuePath.STORESXPATH).send_keys(Keys.ENTER)
        self.click(RevenuePath.PriceSETXPATH)
        self.sleep(1)
        self.click(self.PriceGroup_List()[0])
        self.sleep(1)
        self.click(RevenuePath.LEASEXPATH)
        self.sleep(1)
        self.click(self.Lease_List()[0])
        self.click(self.Lease_List()[1])
        self.click(self.Lease_List()[2])
        self.click(self.Lease_List()[3])
        self.click(self.Lease_List()[4])
        self.click(RevenuePath.AdjustTheWayXPATH)
        self.sleep(1)
        self.click(self.AdjustWay_List()[0])
        self.sleep(1)
        self.click(RevenuePath.qDate)
        self.sleep(1)
        self.clear(RevenuePath.BEGINDATE)
        self.input(RevenuePath.BEGINDATE, Time().localtime())
        self.clear(RevenuePath.ENDDATE)
        self.input(RevenuePath.ENDDATE, Time().get_day_of_day(90))
        self.click(RevenuePath.btnSearchID)
        self.sleep(5)

    # 车价组调价查询

    def CarSetPricing_one(self):
        self.click(RevenuePath.GroupPriceXPATH)
        self.sleep(5)
        self.find_element(RevenuePath.CITYXPATH).send_keys(Keys.SPACE)
        self.sleep(1)
        self.input(RevenuePath.CITYXPATH, "上海")
        self.sleep(1)
        self.find_element(RevenuePath.CITYXPATH).send_keys(Keys.ENTER)
        self.clear(RevenuePath.STORESXPATH)
        self.find_element(RevenuePath.STORESXPATH).send_keys(Keys.SPACE)
        self.sleep(1)
        self.input(RevenuePath.STORESXPATH, "八万人体育场店")
        self.sleep(1)
        self.find_element(RevenuePath.STORESXPATH).send_keys(Keys.ENTER)
        self.click(RevenuePath.PriceSETXPATH)
        self.sleep(1)
        self.click(self.PriceGroup_List()[0])
        self.sleep(1)
        self.click(RevenuePath.LEASEXPATH)
        self.sleep(1)
        self.click(self.Lease_List()[0])
        self.click(self.Lease_List()[1])
        self.click(self.Lease_List()[2])
        self.click(self.Lease_List()[3])
        self.click(self.Lease_List()[4])
        self.click(RevenuePath.AdjustTheWayXPATH)
        self.sleep(1)
        self.click(self.AdjustWay_List()[0])
        self.sleep(1)
        self.click(RevenuePath.btnSearchID)
        self.sleep(1)
        if self.is_element_exsit(RevenuePath.ISElementExsit_1) == True:
            print("############租期1天可见############")
        else:
            print("############租期1天不可见############")
        if self.is_element_exsit(RevenuePath.ISElementExsit_3) ==True:
            print("############租期3天可见############")
        else:
            print("############租期3天不可见############")
        if self.is_element_exsit(RevenuePath.ISElementExsit_5) == True:
            print("############租期5天可见############")
        else:
            print("############租期5天不可见############")
        if self.is_element_exsit(RevenuePath.ISElementExsit_7) == True:
            print("############租期7天可见############")
        else:
            print("############租期7天不可见############")

    # test
    def store_chose(self):
        self.click(RevenuePath.GroupPriceXPATH)
        self.sleep(3)
        self.input(RevenuePath.CITYXPATH, "上海")
        self.sleep(4)
        self.find_element(RevenuePath.CITYXPATH).send_keys(Keys.ENTER)
        for i in range(len(self.storeList())):
            try:
                self.clear(RevenuePath.STORESXPATH)
                self.find_element(RevenuePath.STORESXPATH).send_keys(Keys.SPACE)
                self.sleep(1)
                self.click(self.storeList()[i])
            except Exception as e:
                print(self.storeList()[i], e)


    # 同步值
    def Synchronous_value (self) :
        global Synchronous_value_val
        Synchronous_value_val = 100
        self.clear(RevenuePath.HopePrice)
        self.input(RevenuePath.HopePrice, Synchronous_value_val)
        self.click(RevenuePath.SynchronousValue)
        self.check_value(Synchronous_value_val)
        return Synchronous_value_val


    # 批量生效
    def Mass_Effect(self):
        global Mass_Effect_val
        Mass_Effect_val = 100
        self.click(RevenuePath.MASSEFFECT)
        self.sleep(2)
        # self.click(RevenuePath.btnSubmit_ID)

        self.check_value(Mass_Effect_val)
        return Mass_Effect_val


    # 更新至同城
    def updateCity (self) :
        self.clear(RevenuePath.HopePrice)
        self.input(RevenuePath.HopePrice, val_A)
        self.click(RevenuePath.SynchronousValue)
        self.click(RevenuePath.UPDATECITY)
        self.sleep(2)

        self.click(RevenuePath.btnSubmitSyncStorePrice)
        self.sleep(2)
        self.alert_is_present()
        self.sleep(2)
        for i in range(len(self.storeList())):
            self.clear(RevenuePath.STORESXPATH)
            self.sleep(1)
            self.find_element(RevenuePath.STORESXPATH).send_keys(Keys.SPACE)
            self.sleep(2)
            self.click(self.storeList()[i])
            self.click(RevenuePath.btnSearchID)
            self.check_value(val_A)
        return val_A

    # 门店价格数据同步
    def store_price_synchronous_lease_one(self):
        val = 100
        self.store_price_synchronous_one(20)
        self.sleep(5)
        self.click(RevenuePath.btnSubmitSyncStorePrice)
        self.sleep(2)
        self.alert_is_present()
        for i in range(len(self.storeList())):

            self.sleep(1)
            self.clear(RevenuePath.STORESXPATH)
            self.sleep(2)
            self.find_element(RevenuePath.STORESXPATH).send_keys(Keys.SPACE)
            self.sleep(1)
            try:
                self.click(self.storeList()[i])
            except Exception as e:
                print(e)
                continue
            self.sleep(2)
            self.click(RevenuePath.btnSearchID)
            self.sleep(2)
            self.check_value(val+20)
            return val+20


    # 门店价格数据同步

    def store_price_synchronous_lease_more(self):
        val = 100
        self.store_price_synchronous_more(20)
        self.sleep(2)
        self.click(RevenuePath.btnSubmitSyncStorePrice)
        self.sleep(2)
        self.alert_is_present()
        for i in range(len(self.storeList())):
            self.clear(RevenuePath.STORESXPATH)
            self.sleep(2)
            self.find_element(RevenuePath.STORESXPATH).send_keys(Keys.SPACE)
            self.sleep(1)
            self.click(self.storeList()[i])
            self.sleep(2)
            self.click(RevenuePath.btnSearchID)
            self.sleep(2)
            self.check_value(val + 20)
            self.sleep(2)






    # 门店价格数据同步
    def store_price_synchronous_one(self, money):
        self.click(RevenuePath.STORE_PRICE)
        self.sleep(2)
        self.click(RevenuePath.EditSyncStorePrice)
        self.sleep(2)
        self.click(self.EditSyncStorePrice_list()[0])
        self.click(RevenuePath.A)
        self.clear(RevenuePath.growthmoney)
        self.input(RevenuePath.growthmoney, int(money))

    # 门店价格数据同步
    def store_price_synchronous_more(self, money):
        self.click(RevenuePath.STORE_PRICE)
        self.sleep(2)
        self.click(RevenuePath.EditSyncStorePrice)
        self.click(self.EditSyncStorePrice_list()[0])
        self.click(self.EditSyncStorePrice_list()[1])
        self.click(self.EditSyncStorePrice_list()[2])
        self.click(self.EditSyncStorePrice_list()[3])
        self.click(self.EditSyncStorePrice_list()[4])
        self.clear(RevenuePath.growthmoney)
        self.input(RevenuePath.growthmoney, int(money))


    # 城市价格数据同步

    def city_price_synchronous(self):
        val = 100
        self.click(RevenuePath.btnSyncCityPrice)
        self.sleep(2)
        self.click(RevenuePath.CITYPRICE_LEASE)
        for i in range(len(self.city_lease_List())):
            try:
                self.click(self.city_lease_List()[i])
            except Exception as e:
                print(self.city_lease_List()[i], e)
        self.clear(RevenuePath.CITYPRICE_MANEY)
        self.input(RevenuePath.CITYPRICE_MANEY, 20)
        self.input(RevenuePath.CITYPRICE_CITY, '郑州')
        self.sleep(1)
        self.find_element(RevenuePath.CITYPRICE_CITY).send_keys(Keys.ENTER)
        self.click(RevenuePath.btnSubmitSyncCityPrice)
        self.sleep(1)
        self.alert_is_present()
        self.sleep(2)
        self.clear(RevenuePath.CITYXPATH)
        self.sleep(2)
        self.find_element(RevenuePath.CITYXPATH).send_keys(Keys.SPACE)
        self.sleep(1)
        self.input(RevenuePath.CITYXPATH, '郑州')
        self.sleep(1)
        self.find_element(RevenuePath.CITYXPATH).send_keys(Keys.ENTER)
        self.sleep(1)
        for j in range(len(self.storeList())):
            try:
                self.clear(RevenuePath.STORESXPATH)
                self.sleep(1)
                self.find_element(RevenuePath.STORESXPATH).send_keys(Keys.SPACE)
                self.sleep(1)
                self.click(self.storeList()[j])
                self.click(RevenuePath.btnSearchID)
                self.sleep(2)
                self.check_value(val+20)
            except Exception as e:
                print('门店遍历完成', e)
                break






    # 获取门店价格数据更新 页面中所有属于上海的门店 名称

    def store_synchronous_Name_List(self):
        storeNameList = []
        for i in range(len(self.storeList())):
            name = self.element_text(self.storeList()[i])
            storeNameList.append(name)
        return storeNameList

    # 门店价格同步 门店信息列表
    def store_synchronous_List(self):
        storelist = []
        for i in range(1, 7):
            storeXpath = 'xpath=>/html/body/div[15]/div/div[{i}]'.format(i=i)
            storelist.append(storeXpath)
        return storelist


    # 门店信息列表
    def storeList(self):
        storelist = []
        for i in range(1, 55):
            storeXpath = 'xpath=>/html/body/div[7]/div/div[{i}]'.format(i=i)
            storelist.append(storeXpath)
        return storelist


    # 验证同步值的方法
    def check_value(self, value) :
        try:
            for i in range(len(self.HopePrice_OneDay_List())):
                # print(self.HopePrice_OneDay_List()[i])
                # print(self.get_Attribute(self.HopePrice_OneDay_List()[i],"value"))
                if self.get_Attribute(self.HopePrice_OneDay_List()[i],"value") == '{value}'.format(value=value*1):
                    print("###同步值第1天测试通过###")
                else:
                    print("###同步值第1天测试未通过###")
            for i in range(len(self.HopePrice_ThreeDay_List())):
                if self.get_Attribute(self.HopePrice_ThreeDay_List()[i],"value") == '{value}'.format(value=value*3):
                    print("###同步值第3天测试通过###")
                else:
                    print("###同步值第3天测试未通过###")
            for i in range(len(self.HopePrice_FiveDay_List())):
                if self.get_Attribute(self.HopePrice_FiveDay_List()[i],"value") == '{value}'.format(value=value*5):
                    print("###同步值第5天测试通过###")
                else:
                    print("###同步值第5天测试未通过###")
            for i in range(len(self.HopePrice_Seven_List())):
                if self.get_Attribute(self.HopePrice_Seven_List()[i],"value") == '{value}'.format(value=value*7):
                    print("###同步值第7天测试通过###")
                else:
                    print("###同步值第7天测试未通过###")
            for i in range(len(self.HopePrice_Twenty_eight_List())):
                if self.get_Attribute(self.HopePrice_Twenty_eight_List()[i], "value") != '{value}'.format(value=value*28):
                    print("###同步值第28天测试通过###")
                else:
                    print("###同步值第28天测试未通过###")
        except Exception as e:
            print("####同步值测试异常####", e)





    def EditSyncStorePrice_list(self):
        EditSyncStorePricelist = []
        for i in range(1, 6):
            EditSyncStorePriceXPATH = 'xpath=>/html/body/div[16]/div/div[{i}]'.format(i=i)
            EditSyncStorePricelist.append(EditSyncStorePriceXPATH)
        return EditSyncStorePricelist

    # 将价格组下所有路径添加到列表中
    def PriceGroup_List(self):
        PriceGrouplist = []
        for i in range(1, 11):
            PriceGroupXPATH = "xpath=>/html/body/div[8]/div/div[{i}]".format(i=i)
            PriceGrouplist.append(PriceGroupXPATH)
        return PriceGrouplist

    # 将租期下所有路径添加到列表中
    def Lease_List(self):
        leaselist = []
        for i in range(1, 6):
            leaseXpath = "xpath=>/html/body/div[5]/div/div[{i}]".format(i=i)
            leaselist.append(leaseXpath)
        return leaselist

    # 将调整方式下所有路径添加到列表中
    def AdjustWay_List(self):
        AdjustWaylist = []
        for i in range(1, 3):
            AdjustWayXpath = "xpath=>/html/body/div[9]/div/div[{i}]".format(i=i)
            AdjustWaylist.append(AdjustWayXpath)
        return AdjustWaylist

    # 第一天期望值的路径列表
    def HopePrice_OneDay_List(self):
        HopePricelist = []
        for i in range(2, 9):
            HopePriceXpath = "xpath=>//*[@id=\"dataList\"]/div[1]/div[1]/div[2]/div[4]/table/tbody/tr[2]/td[{i}]/input".format(i=i)
            HopePricelist.append(HopePriceXpath)
        return HopePricelist

    # 第三天期望值的路径列表
    def HopePrice_ThreeDay_List(self):
        HopePricelist = []
        for i in range(2, 7):
            HopePriceXpath = "xpath=>//*[@id=\"dataList\"]/div[1]/div[1]/div[2]/div[4]/table/tbody/tr[10]/td[{i}]/input".format(i=i)
            HopePricelist.append(HopePriceXpath)
        return HopePricelist

    # 第五天期望值的路径列表
    def HopePrice_FiveDay_List(self):
        HopePricelist = []
        for i in range(2, 5):
            HopePriceXpath = "xpath=>//*[@id=\"dataList\"]/div[1]/div[1]/div[2]/div[4]/table/tbody/tr[18]/td[{i}]/input".format(i=i)
            HopePricelist.append(HopePriceXpath)
        return HopePricelist

    # 第七天期望值的路径列表

    def HopePrice_Seven_List(self):
        HopePricelist = []
        for i in range(2, 3):
            HopePriceXpath = "xpath=>//*[@id=\"dataList\"]/div[1]/div[1]/div[2]/div[4]/table/tbody/tr[26]/td[{i}]/input".format(i=i)
            HopePricelist.append(HopePriceXpath)
        return HopePricelist

    # 第28天期望值的路径列表
    def HopePrice_Twenty_eight_List(self):
        HopePricelist = []
        for i in range(2, 9):
            HopePriceXpath = "xpath=>//*[@id=\"dataList\"]/div[1]/div[1]/div[2]/div[4]/table/tbody/tr[34]/td[{i}]/input".format(i=i)
            HopePricelist.append(HopePriceXpath)
        return HopePricelist


    # 将租期下所有路径添加到列表中
    def city_lease_List(self):
        leaselist = []
        for i in range(1, 6):
            leaseXpath = "xpath=>/html/body/div[16]/div/div[{i}]".format(i=i)
            leaselist.append(leaseXpath)
        return leaselist

if __name__ == '__main__':
    print(val_A)
    print(len(Pricing(object).HopePrice_OneDay_List()))
    print(Pricing(object).store_synchronous_Name_List())


