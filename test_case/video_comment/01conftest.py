# -*- coding: utf-8 -*-
# @Time : 2021/10/14 13:49
# @Author : Limusen
# @File : conftest


import time
import pytest
from common.base_page import ElementActions
from common.driver_util import AppiumTest


@pytest.fixture()
def start_app():
    app_driver = AppiumTest().get_driver()
    return app_driver
