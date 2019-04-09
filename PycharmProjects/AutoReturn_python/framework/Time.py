#-*- coding:utf-8 -*-
#! /usr/bin/python
import time
from datetime import date, timedelta

class Time():



    def localtime(self, timeformat='%m/%d/%Y'):
        # 日期格式月日年
        localtime = time.localtime()
        localtime = time.strftime(timeformat, localtime)
        return localtime

    def get_day_of_day(self, n=0, timeformat='%m/%d/%Y'):
        if (n<0):
            n = abs(n)
            a = str(date.today()-timedelta(days=n))
            timea = time.strptime(a, '%Y-%m-%d')
            timea = time.strftime(timeformat, timea)
            return timea
        else:
            a = str(date.today()+timedelta(days=n))
            timea = time.strptime(a, '%Y-%m-%d')
            timea = time.strftime(timeformat, timea)
            return timea

if __name__ == '__main__':
    Time = Time()
    print(Time.localtime())
    print(Time.get_day_of_day(90))