#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/16 16:45
# @Author  : limusem
# @File    : demo_yaml.py
# @Software: PyCharm
# @Description:


from common.driver_util import AppiumTest
from common.base_page import ElementActions
from common.old_yaml_utils import YamlUtils
from common.logs_utils import logger

data = YamlUtils()

class DemoPages(ElementActions):

    def __init__(self, driver):
        super().__init__(driver)

    def click_add(self):
        self.wait(1)
        self.click_yaml(data.get_one_data("add"))

    def click_newpeople(self):
        self.wait(1)
        self.click_yaml(data.get_one_data('newpeople'))

    def input_lastname(self, text):
        self.wait(1)
        self.input_yaml(data.get_one_data('lastname'), text)

    def input_name(self, text):
        self.wait(1)
        self.input_yaml(data.get_one_data('name'), text)

    def input_phone(self,phone):
        self.wait(1)
        self.input_yaml(data.get_one_data('phone'),phone)

    def click_img(self):
        self.wait(1)
        self.click_yaml(data.get_one_data('img'))

    def click_chioce_img(self):
        self.wait(1)
        self.click_yaml(data.get_one_data('chioce_img'))
