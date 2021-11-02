# -*- coding: utf-8 -*-
# @Time : 2021/11/2 11:40
# @Author : Limusen
# @File : demo


import pytest

# def f():
#     return 3
#
#
# def test_function():
#     a = f()
#     assert a % 2 == 0, "判断a为偶数,当前a值为: %s" % a

# 测试登录数据
test_login_data = [("admin", "1111"), ("admin", "")]


def login(user, psw):
    """普通登录函数"""
    print("登录账号: %s" % user)
    print("登录密码: %s" % psw)
    if psw:
        return True
    else:
        return False


@pytest.mark.parametrize("user,psw", test_login_data)
def test_login(user, psw):
    result = login(user, psw)
    assert result == True, "失败原因,密码为空"


if __name__ == '__main__':
    pytest.main()
