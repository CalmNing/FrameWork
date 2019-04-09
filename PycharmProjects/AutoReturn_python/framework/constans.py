#  -*- coding: utf-8 -*-


class Constans():

    # cre_two
    PICK_UP_THE_CITY = "PickupCity"
    PICK_UP_THE_CITY_ID = "PickUpCityId"
    PICK_UP_THE_SHOP = "getStore"
    PICK_UP_THE_SHOP_ID = "getStoreId"
    RETURN_THE_CITY = "ReturnCity"
    RETURN_THE_CITY_ID = "ReturnCityId"
    RETURN_THE_SHOP = "retStore"
    RETURN_THE_SHOP_ID = "retStoreId"

    DELIVERY_TO_THE_DOOR = "id=>getCheck"
    TWO_TOLL = "xpath=>//*[@id=\"addresslist\"]/li[2]/div[2]"
    TWO_TOLL_CLICK = "xpath=>//*[@id=\"addresslist\"]/li[2]/div[4]/input"
    PICK_UP_THE_CAR = "id=>retCheck"
    FOUR_TOLL = "xpath=>//*[@id=\"addresslist\"]/li[4]/div[2]"
    FOUR_TOLL_CLICK = "xpath=>//*[@id=\"addresslist\"]/li[4]/div[4]/input"

    DETERMINE_THE_CITY = "xpath=>//*[@id=\"cityAutoBox\"]/ul/li/a"  # 确定取车城市
    DETERMINE_THE_SHOP = "xpath=>//*[@id=\"ydkBox\"]/div[2]/ul/li[1]/div[1]/dl/dd[1]/span/em"  # 浦东机场T1店
    RETURN_CITY = "id=>ReturnCity"  # 还车城市
    DETERMINE_THE_RETURN_SHOP = "xpath=>//*[@id=\"ydkBox\"]/div[2]/ul/li[1]/div[1]/dl/dd[1]/span/em"  # 浦东机场T1店
    RETURN_CAI_TIME = "xpath=>//*[@id=\"form0\"]/div[1]/ul[2]/li[2]/label"
    BTN_SUBMIT = "id=>btnSubmit"
    GET_MOVE_ELEMENT = "xpath=>//*[@id=\"reservationList\"]/div[1]/ul/li[3]/p[1]/span[3]"
    FLASH_RENT = "xpath=>//*[@id=\"reservationList\"]/div[1]/ul/li[2]/div/div/p[5]/span[2]"
    FLASH_RENTAL_PRICE = ""  # 闪租价格暂时没写
    PAY_AT_THE_STORE1 = "xpath=>//*[@id=\"reservationList\"]/div[1]/ul/li[3]/p[1]/span[4]/a[2]"
    RETURN_PRICE1 = "xpath=>//*[@id=\"reservationList\"]/div[1]/ul/li[3]/p[1]/span[4]/a[3]"
    PACKAGE_PRICE1 = "xpath=>//*[@id=\"reservationList\"]/div[1]/ul/li[3]/p[1]/span[4]/a[4]"
    PAY_AT_THE_STORE2 = "xpath=>//*[@id=\"reservationList\"]/div[1]/ul/li[3]/p[1]/span[4]/a[1]"
    RETURN_PRICE2 = "xpath=>//*[@id=\"reservationList\"]/div[1]/ul/li[3]/p[1]/span[4]/a[2]"
    PACKAGE_PRICE2 = "xpath=>//*[@id=\"reservationList\"]/div[1]/ul/li[3]/p[1]/span[4]/a[3]"
    # choose_time
    PICK_UP_TIME_ID = "getHour"
    PICK_UP_TIME_VALUE = "hdnPickupHour"
    PICK_UP_SHOP = "xpath=>//*[@id=\"form0\"]/div[1]/ul[1]/li[2]/label[1]"
    RETURN_TIME_ID = "retHour"
    RETURN_TIME_VALUE = "hdnReturnHour"

    # cre-three
    UPGRADE_ELEMENT = "id=>upgradetitle"
    ONE_UPGRADE = "xpath=>//*[@id=\"mshowbox\"]/div/div/div/div[1]/div[1]/div[1]/input"
    CLICK_OK_TO_UPGRADE = "xpath=>//*[@id=\"mshowbox\"]/div/div/div/div[2]/p[1]/input"
    CLOSE_THE_POPUP = "xpath=>//*[@id=\"mshowbox\"]/div/a"
    PROMOTION_TEXT = "id=>PromotionCode"                                               # 优惠编码文字
    PROMOTION_SELECT = "xpath=>//*[@id='promotioncodediv']/div[1]"                  # 选择第一张优惠编码

    DESIGNATED_MODEL = "id=>zdcx"
    DESIGNATED_MODEL_VAL = "xpath=>//*[@id=\"gcid\"]/div/div[1]/input"
    BASIS_MODEL = "id=>231"
    ADVANCED_MODEL = "id=>232"
    EXCEPTIONAL_MODEL = "id=>233"
    INVINCIBLE_MODEL = "id=>238"
    AIRPORT_PICKUP = "id=>209"
    NO_OIL = "id=>234"
    UP = "xpath=>//*[@id=\"servicePriceList\"]/em/i[2]"
    DELAYED_RETURN = "id=>235"

    SHOP_TIME1 = "xpath=>//*[@id=\"wrap\"]/div[2]/div/div[1]/div[1]/div[2]"
    CAR_RENTAL_FEES1 = "xpath=>//*[@id='baseRatePrice']/em"
    BASE_SECURITY_FEES1 = "xpath=>//*[@id=\"priceall\"]/div/ul/li[2]"               # 基本保险费文字
    BASE_SECURITY_FEES1_VAL1 = "xpath=>//*[@id='priceall']/div/ul/li[2]/em"         # 基本保险费 价格
    BASE_SECURITY_FEES1_VAL2 = "xpath=>//*[@id='priceall']/div/ul/li[3]/em"          # 基本保险费  价格
    OTHER_SERVER_FEES1 = "xpath=>//*[@id='servicePriceList']/em"                      # 其他服务费
    DISCOUNT_FEES1 = "id=>promotionPriceList"                                         # 优惠折扣文字
    DISCOUNT_FEES1_VAL1 = "xpath=>//*[@id='promotionPriceList']/em"                   # 优惠折扣
    TOTAL_PRICE1 = "id=>priceTotal"
    CRE_SUBMIT_ORDERS = "id=>btnSubmit"                                              # create时提交订单
# "xpath=>//*[@id='priceall']/div/ul/li[2]"

    # cre_four
    GET_ORDER_NUMBER = "xpath=>//*[@id=\"divOrderInfo\"]/span[1]"                     # 获取页面上的订单号
    CLICK_JUMP = "xpath=>//*[@id=\"wrap\"]/div[1]/div[2]/div/a"                      # 创建完订单step4跳转booking
    CLICK_TO_LOGIN = "id=>linkLogin"                                                    # booking点击登录
    MY_LOGIN_PT = "xpath=>//form/div/div/div/div[1]/div[2]/label[2]"                # 普通登录
    MY_LOGIN_NAME = "id=>txtLoginName"                                                  # 登录名
    MY_LOGIN_PASSWORD = "id=>txtPassword"                                               # 密码
    MY_LOGIN_PIC = "id=>txtcaptcha"                                                     # 验证码
    CLICK_ON = "id=>ahrLogin"

    # cre_booking
    MY_YI_HAI_CLICK = "xpath=>//*[@id=\"Form1\"]/div[3]/div[1]/div[1]/div/div[1]/a"       # 点击我的一嗨
    CHOOSE_LOGIN_TYPE = "xpath=>//*[@id=\"content\"]/div/div[2]/dl/dd[1]/a"                # 订单管理
    CLICK_ORDER_MANAGE = "xpath=>//*[@id=\"content\"]/div/div[1]/div[2]/div[1]/ul/li[2]/a" # 预约中
    GET_BEFORE_MONEY = "xpath=>//*[@id=\"content\"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]/a" # 点击第一个预约订单
    SHOP_TIME2 = "xpath=>//*[@id=\"content\"]/div/div[1]/div[2]/div[2]"  # 核对创建订单的门店信息
    CAR_RENTAL_FEES2 = "xpath=>//*[@id=\"J_piceDetail\"]/div/div/div[1]/div[1]/p" # 车辆租赁费文字
    BASE_SECURITY_FEES2 = "xpath=>//*[@id=\"J_piceDetail\"]/div/div/div[2]/div[1]/h3"  # 其他服务费文字
    BASE_SECURITY_FEES2_VAL1 = "xpath=>//*[@id=\"J_piceDetail\"]/div/div/div[2]/div[1]/p"
    BASE_SECURITY_FEES2_VAL2 = "xpath=>//*[@id=\"J_piceDetail\"]/div/div/div[2]/div[2]/h3"
    OTHER_SERVER_FEES2 = "xpath=>//*[@id=\"J_piceDetail\"]/div/div/div[3]/div[1]/p"
    OTHER_SERVER_FEES_DET = "xpath=>//*[@id=\"J_piceDetail\"]/div/div/div[3]/div[2]/ul"
    DISCOUNT_FEES2 = "xpath=>//*[@id=\"J_piceDetail\"]/div/div/div[4]/div[1]/h3" # 优惠折扣文字
    DISCOUNT_FEES2_VAL1 = "xpath=>//*[@id=\"J_piceDetail\"]/div/div/div[4]/div[1]/p"
    TOTAL_PRICE2 = "xpath=>//*[@id=\"J_piceDetail\"]/div/div/div[5]/div[1]/div/span" # 总价文字

    # mod_two
    RETURN_SHOP_TEXT = "xpath=>//*[@id=\"orderpage\"]/div/div[2]/div[2]/h4" # 点击还车城市的文字
    RECALCULATE_PRICE = "id=>chkRecalc"
    PICK_MODEL = "id=>btnSubmit"

    # mod_four
    CLICK_JUMP = "xpath=>//*[@id=\"wrap\"]/div[1]/div[2]/div/a"

    # mod_booking
    CLICK_CANCEL_ORDER = "id=>btn-cancel"
    CANCEL_REASON = "xpath=>//*[@id=\"cancelOrder\"]/div[2]/ul/li[1]/span"
    CANCEL = "id=>cancelConfirm"
