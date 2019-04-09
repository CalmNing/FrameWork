# -*- coding:utf-8 -*-
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    # 获取当前目录的绝对路径
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    # 拼接谷歌驱动地址
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    # 拼接Ie驱动地址
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    # 类的实例，并把驱动给到类
    def __init__(self, driver: object) -> object:
        self.driver = driver

    # read the browser type from config.ini file, return the driver

    def open_browser(self, driver: object) -> object:
        """

        :rtype: object
        """
        # 生成配置解析器
        config = configparser.ConfigParser()
        print(config)
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        # 获取配置文件的绝对路径
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        # config.read(file_path,encoding='UTF-8'), 如果代码有中文注释，用这个，不然报解码错误

        # 获取browserType section(章节) 下 名字为browserType option(选项)的值
        browser = config.get("browserType", "browserName")
        # print(browser)
        # 记录操作日志
        logger.info("You had select %s browser." % browser)
        # 获取 testServer section(章节) 下 名字为 URL option(选项)的值
        url = config.get("testServer", "revenue")
        print(url)
        # 记录操作日志
        logger.info("The test server url is: %s" % url)

        # 判断 browser 值的属性名称 获取相对应的驱动
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")


        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    # 退出浏览器操作

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()

# if __name__ == '__main__':
    # BrowserEngine(object).open_browser('revenue',object)
