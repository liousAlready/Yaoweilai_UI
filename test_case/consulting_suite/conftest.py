# -*- coding: utf-8 -*-
# @Time : 2021/10/20 14:38
# @Author : Limusen
# @File : conftest

import pytest
from common.driver_util import AppiumTest


@pytest.fixture(scope='class')
def set_up():
    driver = AppiumTest().get_driver()
    return driver
