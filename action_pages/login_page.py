# -*- coding: utf-8 -*-
# @Time : 2022/3/2 16:46
# @Author : Limusen
# @File : login_page


from common.base_page import ElementActions
from elememt_info_datas.login_suite.login_page import LoginPage


class LoginAction(ElementActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.lg = LoginPage(driver)

    def login(self):
        self.lg.click_my_btn()
        if self.lg.get_is_login_text() == "登录/注册":
            self.lg.click_login()
        else:
            print("false")

