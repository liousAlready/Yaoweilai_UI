"""
======================
Author: 柠檬班-小简
Time: 2020/8/24 21:01
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""
"""
前置
测试数据：18684720553  python

"""

import pytest
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas import login_datas as td


@pytest.mark.usefixtures("back_login")
class TestLogin:

    # 逆向场景 - 登陆失败 - 数据格式无效
    @pytest.mark.parametrize("case", td.invalid_data)
    def test_login_failed_invalid_data(self, case, back_login):
        LoginPage(back_login).login(case["user"], case["passwd"])
        assert LoginPage(back_login).get_error_msg_from_login_area() == case["check"]

    # 正向场景 - 登陆成功
    @pytest.mark.smoke
    def test_login_success(self, back_login):
        LoginPage(back_login).login(*td.valid_user)
        assert HomePage(back_login).is_exit_exist()
