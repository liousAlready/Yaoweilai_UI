# -*- coding: utf-8 -*-
# @Time : 2021/11/2 14:17
# @Author : Limusen
# @File : test_demo_fixture

import pytest

# 测试账号数据
test_user_data = ["admin1", "admin2"]


@pytest.fixture(scope="module")
def login(request):
    user = request.param
    print("登录账号: %s " % user)
    return user


@pytest.mark.parametrize("login_test_data", test_user_data, indirect=True)
def test_login(login):
    """登录用例"""
    a = login
    print("测试用例中login的返回值: %s" % a)
    assert a != ""

if __name__ == '__main__':
    pytest.main(["-s",'-v',"test_demo_fixture.py"])