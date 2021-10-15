# -*- coding: utf-8 -*-
# @Time : 2021/10/11 17:37
# @Author : Limusen
# @File : test_login

import os
import time
from appium import webdriver
from appium.webdriver.webdriver import By
import pytest
from common.base_page import ElementActions


class TestConsulting:

    def test_case_01(self):
        des = {
            "platformName": "Android",
            "platformVersion": "8.1.0",
            "deviceName": "vivo x20",
            "udid": "c6c8c4ce",
            "noReset": True,
            "newCommandTimeout": 30,  # 30s没对手机发送新命令，就断开连接
            "appPackage": "uni.UNIDD11F28",
            "appActivity": "io.dcloud.PandoraEntryActivity",
        }

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
        save = ElementActions(driver)
        driver.implicitly_wait(10)

        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element(By.XPATH,
                            '//android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView').click()
        time.sleep(1)
        save.save_image_to_allure()


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
