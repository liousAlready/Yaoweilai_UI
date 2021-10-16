# -*- coding: utf-8 -*-
# @Time : 2021/10/11 17:37
# @Author : Limusen
# @File : test_login

import os
import time
from appium.webdriver.webdriver import By
import pytest
from common.base_page import ElementActions
from common.config_utils import local_config
from common.driver_util import AppiumTest
from common.yaml_utils import YamlUtils


class TestConsulting:

    @pytest.mark.parametrize('data', YamlUtils().read_yaml(key='app_consulting'))
    def test_case_01(self, data):
        driver = AppiumTest().get_driver()
        consulting = ElementActions(driver)
        caseData = data['caseDatas']
        driver.implicitly_wait(10)
        print(*caseData['my_btn'])

        consulting.click(*caseData['my_btn'])
        # time.sleep(2)
        # consulting.swipe_to_up()
        # time.sleep(1)


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
