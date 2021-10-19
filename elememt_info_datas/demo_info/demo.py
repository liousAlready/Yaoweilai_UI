#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/16 16:45
# @Author  : limusem
# @File    : demo_yaml.py
# @Software: PyCharm
# @Description:


from common.driver_util import AppiumTest
from common.base_page import ElementActions
from common.yaml_utils import YamlUtils
from common.logs_utils import logger
from test_data.demo_pages import DemoPages as de

data = YamlUtils()

class DemoPages(ElementActions):

    def __init__(self, driver):
        super().__init__(driver)

    def click_add(self):
        self.wait(1)
        self.click(de.add)

    def click_newpeople(self):
        self.wait(1)
        self.click(de.newpeople)

    def input_lastname(self, text):
        self.wait(1)
        self.input(de.lastname, text)

    def input_name(self, text):
        self.wait(1)
        self.input(de.name, text)

    def input_phone(self,phone):
        self.wait(1)
        self.input(de.phone,phone)

    def click_img(self):
        self.wait(1)
        self.click(de.img)

    def click_chioce_img(self):
        self.wait(1)
        self.click(de.chioce_img)
