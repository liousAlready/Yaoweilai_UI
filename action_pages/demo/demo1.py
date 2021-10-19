#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/16 17:04
# @Author  : limusem
# @File    : demo1_yaml.py
# @Software: PyCharm
# @Description:


from elememt_info_datas.demo_info.demo import DemoPages


class Demo:

    def __init__(self,driver):
        self.demo = DemoPages(driver)


    def crater_people(self,**kwargs):
        self.demo.implicitly_wait(10)
        self.demo.click_add()
        self.demo.click_newpeople()
        self.demo.input_lastname(kwargs["lastname"])
        self.demo.input_name(kwargs['name'])
        self.demo.input_phone(kwargs['phone'])
        self.demo.click_img()
        self.demo.click_chioce_img()