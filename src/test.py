# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome('E:\\chromedriver')
# driver.get("https://www.baidu.com/")
# locator = (By.ID, "ks")
#
# try:
#     ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
#     driver.find_element_by_id("kw").send_keys('abc')
#     time.sleep(1)  # 为了看效果
# except:
#     print("ele can't find")
# finally:
#     driver.quit()


str = '摘要文dsgasdg ag ga gdgasd fasdfas asga gas gas gas ga本框内1 ，1数字，	字母，特殊字符，空格 ##$#ESSSFFFAfagdgagew234235dfkdjfa垃圾袋发暗地里发地方a LAJDF DS;KGA DSKGA DLF JDF AJF ASDJF GJAS SDFKA;KS摘要文本框内 ，数字，	字母，特殊字符，空格 ##$#ESSSFFFAfagdgagew234235dfkdjfa垃圾袋发暗地里发地方a LAJDF DS;KGA DSKGA DLF JDF AJF ASDJF DGJAS SDFK A;KS摘要文本框内 ，数'

print(len(str))