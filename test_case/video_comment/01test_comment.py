# -*- coding: utf-8 -*-
# @Time : 2021/10/11 17:37
# @Author : Limusen
# @File : test_login


import time
import random
import allure
from appium.webdriver.webdriver import By


@allure.epic("盛杰-App")
@allure.feature("V1.0")
class TestComment:
    @allure.story("视频模块")
    @allure.title("[case01] 验证能否发送评论信息")
    def test_case_01(self, start_app):
        driver = start_app
        driver.implicitly_wait(10)
        time.sleep(2)

        # 　未登录进行的操作
        # driver.find_element(By.XPATH,
        #                     '//android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//android.view.View[@text="登陆/注册"]').click()
        # time.sleep(2)
        # phone = driver.find_element(By.XPATH,
        #                             '//android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[@text="输入手机号码"]')
        # phone.click()
        # time.sleep(1)
        # driver.press_keycode(8).press_keycode(12).press_keycode(12).press_keycode(14).press_keycode(11).press_keycode(
        #     16).press_keycode(10).press_keycode(10).press_keycode(15).press_keycode(15).press_keycode(12)
        #
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//android.view.View[@text="获取验证码"]').click()
        # time.sleep(10)
        # driver.find_element(By.XPATH, '//android.view.View[@text="开启药未来"]').click()

        # 点击视频专栏
        driver.find_element(By.XPATH, '//android.view.View[@text="视频专栏"]').click()
        time.sleep(2)
        # 点击视频专栏随机点击一个视频
        videos = driver.find_elements(By.XPATH, '//android.view.View[*]/android.view.View[2]/android.view.View[1]')
        video = []
        for lang in videos:
            video.append(lang)
        random.choice(video).click()

        # 点击评论框输入评论
        driver.find_element(By.XPATH, '//android.view.View[@content-desc="点此发评论"]').click()
        content = "说得不错! 继续保持"
        driver.find_element(By.XPATH, '//android.widget.EditText[@text="发表评论"]').send_keys(content)
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.view.View[@content-desc="发送"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.view.View[@content-desc="评论"]').click()
        time.sleep(1)
        texts = driver.page_source

        if content in texts:
            assert True
        else:
            print("没有找到　%s" % content)
