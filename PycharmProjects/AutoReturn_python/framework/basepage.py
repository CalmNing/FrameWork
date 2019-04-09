# coding=utf-8
# import PyMouse as PyMouse
import xlrd
import pymysql
import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    # 类的初始化，并把driver给到类
    def __init__(self, driver):
        self.driver = driver

    # 静态方法单独属于本类，不能使用self传参
    @staticmethod

    # 休息时间
    def sleep(seconds):
        time.sleep(seconds)
        # 保存休息时长到日志
        logger.info("Sleep for %d seconds" % seconds)

    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)  # 参数秒
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # 封装显示等待
    def element_wait(self, css, secs=20):

        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0].strip()
        value = css.split("=>")[1].strip()
        # print(value)
        messages = 'Element: {0} not found in {1} seconds.'.format(css, secs)

        if by == "id":
            WebDriverWait(
                self.driver, secs, 1, NoSuchElementException).until(
                EC.presence_of_element_located((By.ID, value)), messages)

        elif by == "xpath":
            WebDriverWait(
                self.driver, secs, 1, NoSuchElementException).until(
                EC.presence_of_element_located((By.XPATH, value)), messages)

        else:
            raise NameError("Please enter the correct targeting elements,'id','xpath'.")


    # 定位元素方法
    def find_element(self, selector):
        """
        :param selector:
        :return: element
        """
        # element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        else:
            selector_by = selector.split('=>')[0].strip()
            selector_value = selector.split('=>')[1].strip()
            if selector_by == "i" or selector_by == 'id':
                element = self.driver.find_element_by_id(selector_value)
            elif selector_by == "x" or selector_by == 'xpath':
                element = self.driver.find_element_by_xpath(selector_value)
            elif selector_by == "c" or selector_by == 'class':
                element = self.driver.find_element_by_class_name(selector_value)
            elif selector_by == "n" or selector_by == 'name':
                element = self.driver.find_element_by_name(selector_value)
            elif selector_by == "l" or selector_by == 'link_text':
                element = self.driver.find_element_by_link_text(selector_value)
            elif selector_by == "p" or selector_by == 'partial_link_text':
                element = self.driver.find_element_by_partial_link_text(selector_value)
            elif selector_by == "t" or selector_by == 'tag_name':
                element = self.driver.find_element_by_tag_name(selector_value)
            elif selector_by == "s" or selector_by == 'selector_selector':
                element = self.driver.find_element_by_css_selector(selector_value)
            else:
                raise NameError("Please enter a valid type of targeting elements.")
            return element

    # 清除-输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)



    # 输入
    def input(self, selector, text):

        el = self.find_element(selector)
        try:
            logger.info("Had type \' %s \' in inputBox" % text)
            el.send_keys(text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)

    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            self.element_wait(selector, secs=20)
            # self.driver.execute_script("arguments[0].scrollIntoView();", el)

        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

        else:
            el.click()



    # 或者网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 点击-输入-点击
    def clicks_input(self, selector, selector1, text):
        e1 = self.find_element(selector)
        try:
            self.sleep(1)
            e1.click()
            e1.send_keys(text)
            e2 = self.find_element(selector1)
            e2.click()
        except Exception as e:
            logger.error("Failed to clicks_input", e)
    # js强点
    def js_click(self,selector):
        self.driver.execute_script("arguments[0].onclick();", selector)

    # 判断页面元素是否存在
    def is_element_exsit(self, locator):
        try:
            self.find_element(locator)
            return True
        except Exception as e:
            return False

    # 获取页面元素
    def get_element(self, locator):
        element = self.find_element(locator)
        return element

    # 获取页面元素文本
    def element_text(self, locator):
        tests = self.find_element(locator).text
        return tests.encode('utf-8')

    def get_Attribute(self, locator, value='value'):
        text = self.find_element(locator).get_attribute(value)
        return text
    # js修改属性值
    def set_js_value(self, id, valuel):
        try:
            js = "document.getElementById('"+id+"').value='"+valuel+"'"
            self.driver.execute_script(js)
        except Exception as e:
            print("网路开始出现异常", e)

    def remove_readonly(self,selector):
        try:
            js = 'document.getElementById("{element}").removeAttribute("readonly");'.format(element=selector)
            print(js)
            self.driver.execute_script(js)
            print("删除js属性成功")
            # input(selector,text)
            # el = self.find_element(selector)
            # el.send_keys(text)
        except Exception as e:
            print("删除js属性失败",e)


    # def remove_readonly_Beta(self,selector):
    #
    #     try:
    #         js = 'document.getElementById("{element}").firstChild.firstChild.firstChild.firstChild.childNodes[3].firstChild.removeAttribute("readonly");'.format(
    #             element=selector)
    #         print(js)
    #         self.driver.execute_script(js)
    #         print("删除js属性成功")
    #
    #     except Exception as e:
    #         print("删除js属性失败",e)

    # def KeyBoard(self):
    #     m = PyMouse()
    #     k = PyKeyboard()
    #
    # 聚焦元素
    def elementsFocus(self,selector):
        target = self.find_element(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)


    # 分配临时id
    def Set_Attribute(self,ClassName,ClassIndex,IdName):

        try:

            js = "document.getElementsByClassName('{ClassName}')['{ClassIndex}'].setAttribute('id','{IdName}');".format(
                ClassName=ClassName,ClassIndex=ClassIndex,IdName=IdName
            )
            print(js)
            self.driver.execute_script(js)
            print('成功给"{element}"赋值新的id："{test}"'.format(element=ClassName,test=IdName))
        except Exception as e:
            print("赋值js属性失败",e)

    # js获取frame页面的title
    def get_frame_title(self,frameid):
        try :
            js = "window.frames['{frameid}'].document.title".format(frameid=frameid)
            # print(js)
            frametitle = self.driver.execute_script(js)
            print('成功获取当前页面的title，title：',frametitle)
            return frametitle

        except Exception as e:
            print("获取子页面的title失败",e)

    # 窗口切换
    def handle(self):
        handles = self.driver.window_handles  # 获取当前全部窗口句柄集合
        print(handles)
        for handle in handles:  # 切换窗口
            if handle != self.driver.current_window_handle:
                print('switch to second window', handle)
                self.close()  # 关闭第一个窗口
            self.driver.switch_to.window(handle)  # 切换到第二个窗口

    # 判断弹框
    def alert_is_present(self):
        try:
            alert = self.driver.switch_to.alert
            print(alert.text)
            alert.accept()
        except Exception as e:
            print("无弹框 ", e)

    # 网址链接
    def link(self, text):
        self.driver.get(text)

    # 跳转iframe窗口
    def goto_iframe(self,selector):
        self.driver.switch_to.frame(selector)




    def mysql_link(self,pickup,dropoff):
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "password", "test")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
    # def select_sql(self,pickup,dropoff):
        sql = "SELECT * FROM city_price WHERE PickupCity = '" + pickup + "'and DropoffCity = '" + dropoff + "'"
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            for row in results:
                id = row[0]
                pickup_city = row[1]
                dropoff_city = row[2]
                mileage = row[3]
                price = row[4]
                unit = row[5]
                total_price = row[6]
                # 打印结果
                print("id=%s, PickupCity=%s, DropoffCity=%s, Mileage=%s, price=%s, unit=%s, TotalPrice=%s" % (
                id, pickup_city, dropoff_city, mileage, price, unit, total_price))
        except Exception as e:
            print("Error: unable to fetch data", e)
            # 关闭数据库连接

        self.db.close()

    def dict_data(excel_path, sheet_name, number):
        data = xlrd.open_workbook(excel_path)
        table = data.sheet_by_name(sheet_name)
        # 获取第一行作为key值
        keys = table.row_values(0)
        # 获取总行数
        row_num = table.nrows
        # 获取总列数
        col_num = table.ncols
        if row_num <= 1:
            print("总行数小于1")
        else:
            rows = table.row_values(number)
            print(rows)


