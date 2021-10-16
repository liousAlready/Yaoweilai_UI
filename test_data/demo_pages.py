#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/16 20:22
# @Author  : limusem
# @File    : demo_pages.py
# @Software: PyCharm
# @Description:


from selenium.webdriver.common.by import By


class DemoPages:
    my_btn = (By.XPATH, '//android.widget.TextView[@text="添加常用联系人"]')


if __name__ == '__main__':
    print(DemoPages.my_btn)
