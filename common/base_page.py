# -*- coding: utf-8 -*-
# @Time : 2021/10/12 15:53
# @Author : Limusen
# @File : action

import os
import time, datetime
import random
import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from common.logs_utils import logger
from common.driver_util import AppiumTest
from common.yaml_utils import YamlUtils


class ElementActions:

    def __init__(self, driver):
        self.driver = driver

    def wait(self, seconds):
        time.sleep(seconds)
        logger.info("休息一下")

    def sysback(self):
        """
        系统的返回按钮
        :return: None
        """
        self.driver.keyevent(4)
        logger.info("点击系统的返回按按钮")

    def get_size(self):
        """
        获取当前屏幕的分辨率
        :return: int, x*y
        """
        size = self.driver.get_window_size()
        logger.info("获取屏幕分辨率: [%s]" % size)
        return size

    def get_text(self, *locator):
        element = self.driver.find_element(*locator)
        try:
            text = element.text
            logger.info("正在获取文本信息: [%s]" % text)
            return text
        except Exception as e:
            logger.error("当前操作报错,原因是: [%s]" % e)
            self.save_image_to_allure()

    def swipe_to_up(self):
        """
        从下往上滑动
        :return: None
        """
        try:
            window_size = self.get_size()
            width = window_size.get("width")
            height = window_size.get("height")
            self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
            logger.info("从下往上滑动")
        except Exception as e:
            logger.error("元素不能识别,原因是: %s" % e)
            self.save_image_to_allure()

    def swipe_to_down(self):
        """
        从上往下滑动
        :return: None
        """
        try:
            window_size = self.get_size()
            width = window_size.get("width")
            height = window_size.get("height")
            self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)
            logger.info("从上往下滑动")
        except Exception as e:
            logger.error("元素不能识别,原因是: %s" % e)
            self.save_image_to_allure()

    def swipe_to_left(self):
        """
        从右往左滑动
        :return: None
        """
        try:
            window_size = self.get_size()
            width = window_size.get("width")
            height = window_size.get("height")
            self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)
            logger.info("从右往左滑动")
        except Exception as e:
            logger.error("元素不能识别,原因是: %s" % e)
            self.save_image_to_allure()

    def swipe_to_right(self):
        """
        从左往右滑动
        :return: None
        """
        try:
            window_size = self.get_size()
            width = window_size.get("width")
            height = window_size.get("height")
            self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)
            logger.info("从左往右滑动")
        except Exception as e:
            logger.error("元素不能识别,原因是: %s" % e)
            self.save_image_to_allure()

    def find_element(self, locator, locator_timeout=5):
        try:
            locator_type = locator['locator_type']
            locator_value = locator['locator_value']

            if locator_type == "name":
                locator_type = By.NAME
            elif locator_type == "css":
                locator_type = By.CSS_SELECTOR
            elif locator_type == "xpath":
                locator_type = By.XPATH
            elif locator_type == "id":
                locator_type = By.ID
            elif locator_type == "class":
                locator_type = By.CLASS_NAME
            elif locator_type == "linktext":
                locator_type = By.LINK_TEXT
            elif locator_type == "partiallink":
                locator_type = By.PARTIAL_LINK_TEXT
            elif locator_type == "tag":
                locator_type = By.TAG_NAME
            element = WebDriverWait(self.driver, locator_timeout).until(
                lambda x: x.find_elements(locator_type, locator_value))
            logger.info('[%s] 元素识别成功' % element)
        except Exception as e:
            logger.error("元素不能识别,原因是: %s" % e)
            self.save_image_to_allure()

    def click(self, *locator):
        element = self.driver.find_element(*locator)
        try:
            element.click()
            logger.info("识别元素进行点击操作...")
        except Exception as e:
            logger.error("当前操作报错,原因是: [%s]" % e)
            self.save_image_to_allure()

    # def click(self, *locator):
    #     element = self.driver.find_element(*locator)
    #     try:
    #         element.click()
    #         logger.info("识别元素进行点击操作...")
    #     except Exception as e:
    #         logger.error("当前操作报错,原因是: [%s]" % e)
    #         self.save_image_to_allure()

    # def find_element(self, *locator, locator_timeout=5):
    #     try:
    #         self.driver.find_element(*locator)
    #         element = WebDriverWait(self.driver, locator_timeout).until(
    #             lambda x: x.find_elements(*locator))
    #         logger.info('[%s] 元素识别成功' % element)
    #     except Exception as e:
    #         logger.error("元素不能识别,原因是: %s" % e)
    #         self.save_image_to_allure()

    def input(self, *locator, text):
        element = self.driver.find_element(*locator)
        try:
            element.input(text)
            logger.info("当前正在进行输入操作:[%s]" % text)
        except Exception as e:
            logger.error("当前操作报错,原因是: [%s]" % e)
            self.save_image_to_allure()

    def get_absolute_path(self):
        current = os.path.dirname(os.path.abspath(__file__))
        logger.info("获取当前项目的路径,方便拼接: [%s]" % current)
        return current

    def save_scree_image(self):
        """
        对当前页面进行截图
        :return:
        """
        try:
            today = time.strftime('%Y_%m_%d_%H_%M_%S')  # 今天
            filename = '{}.png'.format(today)
            error_img = os.path.join(self.get_absolute_path(), '..', 'report', 'img')
            file_path = os.path.join(error_img, filename)
            self.driver.save_screenshot(file_path)
            logger.info("截图成功，图表保存的路径:{}".format(file_path))
            return file_path
        except Exception as e:
            logger.error("当前操作报错,原因是: [%s]" % e)

    def save_image_to_allure(self):
        """
        提供截图方法
        """
        try:
            file_path = self.save_scree_image()
            with open(file_path, "rb") as f:
                file = f.read()
                allure.attach(file, "失败截图", allure.attachment_type.PNG)
        except Exception as e:
            logger.error("截图失败,原因是: %s" % e.__str__())

    def keyboard_input(self, text):
        """
        :param text:  调用adb打开键盘，并输入内容
        :return:
        """
        try:
            time.sleep(2)
            adb1 = "adb shell ime set com.android.adbkeyboard/.AdbIME"
            os.system(adb1)
            time.sleep(2)
            adb2 = "adb shell am broadcast -a ADB_INPUT_TEXT --es msg '%s'" % text
            os.system(adb2)
            logger.info("当前键盘输入的内容是 % s " % text)
        except Exception as e:
            logger.error("当前操作报错,原因是: [%s]" % e)
            self.save_image_to_allure()


if __name__ == '__main__':
    app_driver = AppiumTest().get_driver()
    Element_driver = ElementActions(app_driver)
    datas = YamlUtils().get_one_data("history")
    print(datas)
    Element_driver.find_element(datas)
