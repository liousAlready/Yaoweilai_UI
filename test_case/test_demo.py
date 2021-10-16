#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/16 17:10
# @Author  : limusem
# @File    : test_demo.py
# @Software: PyCharm
# @Description:

import pytest

from common.driver_util import AppiumTest
from action_pages.demo1 import Demo


class TestDemo:

    def test_case_01(self):
        self.driver = AppiumTest().get_driver()
        self.page_driver = Demo(self.driver)
        self.page_driver.crater_people(lastname="里", name="受", phone="15574885663")


if __name__ == '__main__':
    pytest.main(['-s','-v'])