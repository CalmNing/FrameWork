#-*- coding:utf-8 -*-
#! /usr/bin/python
import numpy as np
import os

from PagePath.CrewsTakePricingPath import RevenuePath
from framework.MYSQL_client import insert
from framework.basepage import BasePage
from src.CrewsTakePricing_one import Pricing


__author__ = 'Calm'

"""
    这里面将实现具体的操作方法
    """


class PriceLinkage(Pricing):
    """
    书写所有的车型价格联动的验证方法函数
    """
    global variable
    variable = np.random.randint(low=20, high=100)

    def is_city_config(self, basis_Value)->int:
        """ 勾选城市统一配置
            勾选车型组统一配置
            勾选多租期配置
            按照金额调整

        :return:
        """
        self.click(RevenuePath.btnPriceLinkage)

        self.sleep(3)
        self.click(RevenuePath.is_car_list_configuration)
        self.sleep(20)
        self.click(RevenuePath.LEASEMORECONFIGURATION)
        self.sleep(3)
        priceInputList = self.priceInputList()
        carModelNum = self.carModelNum()
        carListName = self.carListName()
        carListNum = self.carListNum()
        carModelName = self.carModelName()
        for i in range(len(priceInputList)):
            self.sleep(2)
            self.clear(priceInputList[i])
            self.input(priceInputList[i], variable)
            self.sleep(3)
            insert(city=self.pageValue().get('city'),
                   is_city_configuration=1,
                   is_car_list_configuration=1,
                   is_lease_configuration=1,
                   lease_period=1,
                   car_model=self.get_Attribute(carModelName[i], 'textContent'),
                   car_model_number=self.get_Attribute(carModelNum[i], 'textContent'),
                   car_list=self.get_Attribute(carListName[i], 'textContent'),
                   car_list_number=self.get_Attribute(carListNum[i], 'textContent'),
                   storepaying_price=basis_Value + variable
                   )
        self.click(RevenuePath.SAVEBTN)
        self.sleep(50)
        return basis_Value + variable




    def pageValue(self)->dict:
        '''
        获取所有要插入的数据
        :return: dict
        '''
        city = self.get_Attribute(RevenuePath.Pricelinkcity, 'textContent')
        lease = self.get_Attribute(RevenuePath.Pricelinklease, 'textContent')

        vauleDict = {
            'city': city,
            'lease': lease

        }
        return vauleDict







    def priceInputList(self)->list:

        """
        获取所有的金额输入框的路径
        :return:list
        """
        priceInputList = []
        for i in range(1, 1000):
            Input = RevenuePath.CHANGEPRICEINPUT.format(i=i)
            # print(Input)
            if self.is_element_exsit(Input):
                priceInputList.append(Input)
            else:
                print('路径获取完成')
                break
        return priceInputList


    def rateInputList(self)->list:
        '''
        获取所有的比率输入框的路径
        :return: list
        '''
        rateInputList = []
        for i in range(1, 1000):
            Input = RevenuePath.CHANGERATEINPUT.format(i=i)
            if self.is_element_exsit(Input):
                rateInputList.append(Input)
            else:
               print('路径获取完成')
               break

        return rateInputList

    def carListNum(self)->list:
        '''
        获取所有的车组型标号
        :return:
        '''
        carListNum = []
        for i in range(1, 1000):
            numXpath = RevenuePath.CARLISTNUM.format(i=i)
            if self.is_element_exsit(numXpath):
                carListNum.append(numXpath)
            else:
                print('路径获取完成')
                break
        return carListNum

    def carListName(self)->list:
        '''
        获取所有的车组名
        :return:
        '''
        carListName = []
        for i in range(1, 1000):
            carListNameXpath = RevenuePath.CARLISTNAMW.format(i=i)
            if self.is_element_exsit(carListNameXpath):
                carListName.append(carListNameXpath)
            else:
                print('路径获取完成')
                break
        return carListName

    def carModelName(self)->list:
        '''
        获取所有的车型名
        :return:
        '''
        carModelList= []

        for i in range(1, 1000):
            carModelXpath = RevenuePath.CARMODELNAME.format(i=i)

            # print(carModelList1)

            if self.is_element_exsit(carModelXpath):
                carModelList.append(carModelXpath)
                # print(carModelList)
            else:
                print('路径获取完成')
                break
        return carModelList

    def carModelNum(self)->list:
        '''
        获取所有的车型编号
        :return:
        '''
        carModelNumList=[]
        for i in range(1, 1000):
            carModelNumXpath = RevenuePath.CARMODELNUM.format(i=i)
            if self.is_element_exsit(carModelNumXpath):
                carModelNumList.append(carModelNumXpath)
            else:
                print('路径获取完成')
                break
        return carModelNumList




if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath('.')))