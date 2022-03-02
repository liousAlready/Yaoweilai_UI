# -*- coding: utf-8 -*-
# @Time : 2022/3/2 16:41
# @Author : Limusen
# @File : login_data

from selenium.webdriver.common.by import By


class LoginData:
    my_btn = (By.XPATH, '//android.widget.TextView[@text="我的"]')
    is_login = (By.XPATH, '//android.view.View[@text="登录/注册"]')
