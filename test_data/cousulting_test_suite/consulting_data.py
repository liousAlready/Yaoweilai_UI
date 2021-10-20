# -*- coding: utf-8 -*-
# @Time : 2021/10/20 11:26
# @Author : Limusen
# @File : consulting_data
from selenium.webdriver.common.by import By


class ConsultingData:
    my_btn = (By.XPATH, '//android.widget.TextView[@text="我的"]')
    information_btn = (By.XPATH, '//android.view.View[@text="资讯文章"]')
    information_title = (By.XPATH, '//android.view.View[@text="标题（5~38个字）"]')
    information_content = (
        By.XPATH, '//android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View')
    next_btn = (By.XPATH, '//android.view.View[@text="下一步"]')
    only_pic = (By.XPATH, '//android.view.View[@text="单图"]')
    add_pic = (By.XPATH, '//android.view.View[@text="添加封面"]')
    camera_btn = (By.XPATH, '//android.widget.TextView[@text="相册"]')
    screenshot_btn = (By.XPATH, '//android.widget.TextView[@text="截屏"]')
    article_tag = (By.XPATH, '//android.view.View[@text="文章标签"]')
    tag_btn = (By.XPATH, '//android.view.View[4]/android.view.View/android.view.View/android.view.View[1]')  # 标签
    complete_btn = (By.XPATH, '//android.view.View[@text="完成"]')
    release_btn = (By.XPATH, '//android.view.View[@text="发布"]')
