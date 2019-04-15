#encoding:utf-8
#name:mod_config.py

import configparser
import os.path

#获取config配置文件

def getDBConfig(section, key):

    config = configparser.ConfigParser()
    path = os.path.dirname(os.path.abspath('.')) + '\config\db_config.ini'
    # print(path)
    config.read(path)
    return config.get(section, key)

# print(getDBConfig("database", "dbhost"))