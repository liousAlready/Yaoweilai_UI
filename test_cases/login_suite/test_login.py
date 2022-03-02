# -*- coding: utf-8 -*-
# @Time : 2022/3/2 17:00
# @Author : Limusen
# @File : test_login


import pytest
import allure
from action_pages.login_page import LoginAction


class TestLogin:

    def test_case_is_login(self, set_up):
        log = LoginAction(set_up)
        log.login()


if __name__ == '__main__':
    pytest.main(['-s','-v','test_login.py'])
