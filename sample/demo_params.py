# -*- coding: utf-8 -*-
# @Time : 2021/10/20 17:38
# @Author : Limusen
# @File : demo_params


import pytest


@pytest.mark.parametrize("user", ['shichao', 'xiaoming'])
def test_user(user):
    print("============")
    print("user:{}".format(user))
    print("============")


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
