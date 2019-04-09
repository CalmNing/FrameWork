# -*- coding:utf-8 -*-
import logging
import sys

import pymysql

from framework.GetDBconfig import getDBConfig

def insert(city='NUll',
           car_model='NUll',
           car_model_number='NUll',
           car_list='NUll',
           car_list_number='NUll',
           storepaying_price='NUll',
           is_city_configuration=1,
           is_car_list_configuration=2,
           is_lease_configuration=1,
           lease_period=2):

    connection = pymysql.connect(host=getDBConfig("database", "dbhost"),
                                 db=getDBConfig("database", "dbname"),
                                 user=getDBConfig("database", "dbuser"),
                                 password=getDBConfig('database', 'dbpassword'),
                                 charset=getDBConfig("database", "dbcharset"))
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `backgroundchangeprice` (`city`, `is_city_configuration`,`is_car_list_configuration`, `is_lease_configuration`, `lease_period`, `car_model`, `car_model_number`, `car_list`, `car_list_number`, `storepaying_price`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (city,
                                 is_city_configuration,
                                 is_car_list_configuration,
                                 is_lease_configuration,
                                 lease_period,
                                 car_model,
                                 car_model_number,
                                 car_list,
                                 car_list_number,
                                 storepaying_price
                                 )
                           )
        connection.commit()

        # with connectiondatabase.cursor() as cursor:
        #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        #     cursor.execute(sql, ('webmaster@python.org',))
        #     result = cursor.fetchone()
        #     print(result)
    finally:
        connection.close()