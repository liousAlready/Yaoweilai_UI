# -*- coding: utf-8 -*-
# @Time : 2021/10/14 17:39
# @Author : Limusen
# @File : consulting

import pytest
from common.yaml_utils import YamlUtils
from common.base_page import ElementActions
from common.driver_util import AppiumTest


class Consulting(ElementActions):

    def __init__(self, driver):
        super().__init__(driver)
        elements = YamlUtils().get_yaml(key='app_consulting')
        self.caseDate = elements['caseDatas']

    @pytest.mark.parametrize('data', YamlUtils().read_yaml(key='app_consulting'))
    def test_case_01(self, data):
        driver = AppiumTest().get_driver()
        consulting = ElementActions(driver)
        caseData = data['caseDatas']
        driver.implicitly_wait(10)
        print(*caseData['my_btn'])

    def click_my_btn(self):
        self.click(self.caseDate['my_btn'])

    def print_but(self):
        print(self.caseDate['my_btn'])


if __name__ == '__main__':
    driver = AppiumTest().get_driver()
    Consulting(driver).print_but()
    Consulting(driver).click_my_btn()
