#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/16 20:22
# @Author  : limusem
# @File    : demo_pages.py
# @Software: PyCharm
# @Description:


from selenium.webdriver.common.by import By


class DemoPages:
    add = (By.XPATH, '//android.widget.TextView[@text="添加常用联系人"]')
    newpeople = (By.XPATH, ' //android.widget.TextView[@text="创建新联系人"]')
    lastname = (By.XPATH, '//android.widget.EditText[@text="姓氏"]')
    name = (By.XPATH, '//android.widget.EditText[@text="名字"]')
    phone = (By.XPATH, '//android.widget.EditText[@text="电话"]')
    img = (By.XPATH, '//android.widget.ImageView[@resource-id="com.android.contacts:id/photo"]')
    chioce_img = (By.XPATH, '//android.widget.TextView[@text="选择照片"]')


if __name__ == '__main__':
    print(type(DemoPages.add))
    print(DemoPages.add)
