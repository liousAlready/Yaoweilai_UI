# -*- coding: utf-8 -*-
# @Time : 2022/3/2 16:46
# @Author : Limusen
# @File : login_page


from common.base_page import ElementActions
from test_data.login_test_data.login_data import LoginData as lg


class LoginPage(ElementActions):

    def __init__(self, driver):
        super().__init__(driver)

    def click_my_btn(self):
        self.wait(6)
        self.click(lg.my_btn)

    def click_login(self):
        self.wait(2)
        self.click(lg.my_btn)

    def get_is_login_text(self):
        self.wait(2)
        return self.get_text(lg.is_login)
