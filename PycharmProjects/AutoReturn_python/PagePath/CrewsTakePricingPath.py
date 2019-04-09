#-*- coding:utf-8 -*-
#! /usr/bin/python
__author__ = 'Calm'

"""
    这里面将会存储操作也面的所有路径
    """
class RevenuePath():


    """
    login 登录页面定义
    """
    # 账号输入框元素id
    CODE_ID = "id=>accountNo"
    # 密码输入框元素id
    PASSWORD_ID = "id=>password"
    # 登录按钮元素id
    btnSubmit_ID = "id=>btnSubmit"

    """
    
        车组调价
        """

    # 进入车组调价页面

    GroupPriceXPATH = "xpath=>/html/body/div[3]/aside[1]/section/ul/li[1]/ul/li[1]/a"        # 车组调价
    CITYXPATH="xpath=>//*[@id='GroupPrice']/div[1]/ul/li[1]/div/span[1]/input[1]"      #   城市
    STORESXPATH = "xpath=>//*[@id='GroupPrice']/div[1]/ul/li[1]/div/span[2]/input[1]"      #   门店
    STORES_DOWNBOX_XPATH = "xpath=>//*[@id=\"GroupPrice\"]/div[1]/ul/li[1]/div/span[2]/span/a" # 门店下拉框
    # // *[ @ id = "GroupPrice"] / div[1] / ul / li[1] / div / span[2] / span / a
    PriceGroupListID_JS = "id=>GroupPrice"      #价格组js
    ChangePriceGroupListClass_JS = "id=>textbox-text validatebox-text textbox-prompt" # js 需要的属性
    PriceSETXPATH= "xpath=>//*[@id=\"GroupPrice\"]/div[1]/ul/li[1]/div/span[3]/input[1]" # 价格组
    RentalListID_JS = "id=>rentalList"         # 租期js
    LEASEXPATH = "xpath=>//*[@id='GroupPrice']/div[1]/ul/li[2]/div/span/input"     #  租期
    AdjustTypeID_JS = "id=>adjustType"     # 调整方式js
    AdjustTheWayXPATH = "xpath=>//*[@id='GroupPrice']/div[1]/ul/li[3]/div/span/input[1]"   #调整方式
    # 点击日期
    qDate = 'xpath=>//*[@id="qDate"]'
    # 起始日期输入框
    BEGINDATE = 'xpath=>/html/body/div[6]/div[1]/div[1]/input'
    # 截止日期输入框
    ENDDATE = 'xpath=>/html/body/div[6]/div[2]/div[1]/input'
    btnSearchID = "id=>btnSearch"  # 查询
    # 判断元素可见
    ISElementExsit_1 = "xpath=>//*[@id='showPrice']/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/ul/li[4]"
    ISElementExsit_3 = "xpath=>//*[@id='showPrice']/div[1]/div[2]/div[3]/table/tbody/tr[9]/td[1]/ul/li[4]"
    ISElementExsit_7 = "xpath=>//*[@id='showPrice']/div[1]/div[2]/div[3]/table/tbody/tr[17]/td[1]/ul/li[4]"
    ISElementExsit_5 = "xpath=>//*[@id='showPrice']/div[1]/div[2]/div[3]/table/tbody/tr[25]/td[1]/ul/li[4]"

    # 同步值

    HopePrice = "xpath=>//*[@id=\"dataList\"]/div[1]/div[1]/div[2]/div[4]/table/tbody/tr[2]/td[2]/input"  # 期望价格
    # 同步值
    SynchronousValue = "xpath=>//*[@id=\"dataList\"]/div[1]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/ul/li[7]/a"
    # 批量生效
    MASSEFFECT = "xpath=>//*[@id=\"dataList\"]/div[1]/div[1]/div[1]/div/div/button[1]"
    # 更新至同城
    UPDATECITY = "xpath=>//*[@id=\"dataList\"]/div[1]/div[1]/div[1]/div/div/button[2]"
    btnSubmitSyncStorePrice = "id=>btnSubmitSyncStorePrice" # 确认

    ###### 同步门店信息
    STORE_PRICE = 'id=>btnSyncStorePrice'
    EditSyncStorePrice = 'xpath=>//*[@id="EditSyncStorePrice"]/div/div[2]/form/div[5]/div[1]/div/span/input'
    growthmoney = 'xpath=>//*[@id="EditSyncStorePrice"]/div/div[2]/form/div[5]/div[2]/div/input'
    SyncStore = 'xpath=>//*[@id="CustomModal"]/div/div/div[2]/form/div[6]/div/span/input'
    # btnSubmitSyncStorePrice = 'xpath=>//*[@id="btnSubmitSyncStorePrice"]'
    A = 'xpath=>//*[@id="EditSyncStorePrice"]/div/div[1]'

    # 城市价格数据同步按钮
    btnSyncCityPrice = 'id=>btnSyncCityPrice'
    CITYPRICE_LEASE = 'xpath=>//*[@id="EditSyncCityPrice"]/div/div[2]/form/div[4]/div/span/input'
    CITYPRICE_MANEY = 'xpath=>//*[@id="EditSyncCityPrice"]/div/div[2]/form/div[5]/div/input'
    CITYPRICE_CITY = 'xpath=>//*[@id="EditSyncCityPrice"]/div/div[2]/form/div[6]/div/span/input[1]'
    btnSubmitSyncCityPrice = 'id=>btnSubmitSyncCityPrice'

    # 车型价格联动

    btnPriceLinkage = 'id=>btnPriceLinkage'
    # 验证表单是否加载完成
    TABLEIDSPLAYDE = 'xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[7]/label'
    # 获取城市名称路径
    Pricelinkcity = 'xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[1]/div/p'
    # 获取门店名称路径
    Pricelinkstore ='xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[2]/div/p'
    # 获取租期路径
    Pricelinklease = 'xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[5]/div/span/input[2]'
    # 是否城市统一配置
    is_city_configuration = 'xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[6]/div[1]/div/label'
    # 车组统一配置
    is_car_list_configuration = 'xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[6]/div[2]/div/label'
    # 多租期配置
    LEASEMORECONFIGURATION = 'xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[6]/div[3]/div/label'
    # 获取车组编号
    CARLISTNUM = 'xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[7]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[{i}]/td[2]'
    # 获取车组名
    CARLISTNAMW= 'xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[7]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[{i}]/td[3]'
    # 获取车型编号
    CARMODELNUM = 'xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[7]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[{i}]/td[4]'
    # 获取车型名
    CARMODELNAME = 'xpath=>//*[@id="EditGroupCarTypePriceLinkage"]/div/div[2]/form/div[7]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[{i}]/td[5]'
    # 金额调整输入框
    CHANGEPRICEINPUT = 'xpath=>//*[@id="CustomModal"]/div/div/div[2]/form/div[7]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[{i}]/td[6]/input'
    # 比率调整输入框
    CHANGERATEINPUT = 'xpath=>//*[@id="CustomModal"]/div/div/div[2]/form/div[7]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[{i}]/td[7]/input'
    # 保存按钮
    SAVEBTN = 'xpath=>//*[@id="btnSubmitPriceLinkage"]'






"""
定义 ehi家园的也路径

"""
class ehaihr_xpath():

    Code_id = "id=>t_Username"      # 工号
    PassWord = "id=>t_Password"     # 密码
    LoginButton_id = "id=>b_Login"      # 登录按钮
    IFRAME_id = "id=>rightFrame"        # 框架id
    BXID = "id=>BX"     # 报销id
    HTID = "id=>HT"     # 合同id
    XZGLID = "id=>XZ"     # 行政管理id
    QXID = "id=>QX"     # 权限id
    EHIQW = "xpath=>//*[@id=\"main-content\"]/ul/li[7]/a"     # 企业文化xpath
    XSXSID = "id=>XS"     # 销售线索id
    OAXTID= "id=>OA"     # OAid
    XIWTFKID= "id=>rs_SystemFeedback"     # 系统问题反馈id
    QJJBCXID = 'id=>rs_LeaveSearch'     # 请假加班查询id
    XZCXID = 'id=>rs_SalaryInfo'     # 薪资查询id
    BXSQID = 'id=>bx_ExpenseApply'     # 报销申请id
    BXCXID = 'id=>bx_ExpenseSearch'     # 报销查询id
    TTHCXID = 'id=>bx_InvoiceSearch'     # 抬头税号查询id
    QYXS_TGLJ = 'id=>rs_FullSales'     # 权益销售推广链接id

