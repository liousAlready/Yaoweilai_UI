"""
======================
Author: 柠檬班-小简
Time: 2020/8/26 21:26
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By

class HomePageLocs:
    # 退出按钮
    exit_loc = (By.XPATH, '//a[text()="退出"]')
    # 关于我们
    about_us = (By.XPATH, '//a[text()="关于我们"]')
    # 用户昵称
    user_link = (By.XPATH, '//a[@href="/Member/index.html"]')
    # 抢投标按钮
    bid_button = (By.XPATH, '//a[@class="btn btn-special"]')