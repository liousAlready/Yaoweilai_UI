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


class TestConsulting:

    def test_case_01(self):
        driver = AppiumTest().get_driver()
        consulting = ElementActions(driver)

        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element(By.XPATH,
                            '//android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView').click()
        time.sleep(1)
        qiyeruzhu = driver.find_element(By.XPATH, '//android.view.View[@text="企业入驻"]')
        see_history = driver.find_element(By.XPATH, '//android.view.View[@text="观看历史"]')
        driver.scroll(qiyeruzhu, see_history)
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.view.View[@text="资讯文章"]').click()

        # 输入标题
        driver.find_element(By.XPATH,
                            '//android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText').send_keys(
            local_config.get_consultation_title)

        driver.find_element(By.XPATH,
                            '//android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[@index="0"]').click()
        time.sleep(3)

        consulting.keyboard_input(local_config.get_consultation_content)
        consulting.save_image_to_allure()
        time.sleep(2)
        driver.find_element(By.XPATH, '//android.view.View[@text="下一步"]').click()

        driver.find_element(By.XPATH, '//android.view.View[@text="文章标签"]').click()

        # 标签有敏感词还不能随机取值
        # num = []
        # for i in range(1, 11):
        #     num.append(i)
        # random.choice(num)
        # time.sleep(1)
        # tag = driver.find_element(By.XPATH, '//android.view.View[4]/android.view.View[1]/android.view.View[%s]' % num)
        # tag.click()
        # time.sleep(1)

        driver.find_element(By.XPATH, '//android.view.View[4]/android.view.View[1]/android.view.View[4]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.view.View[@text="完成"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.view.View[@text="发布"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//android.view.View[@text="作品"]').click()
        time.sleep(3)
        # 不能点击资讯，就靠滑动翻页进行定位信息
        driver.flick(start_x=815, start_y=879, end_x=219, end_y=879)
        time.sleep(3)
        driver.flick(start_x=815, start_y=879, end_x=219, end_y=879)
        time.sleep(5)
        consulting.save_image_to_allure()



if __name__ == '__main__':
    pytest.main(['-s', '-v'])
