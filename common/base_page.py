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
from test_data.demo_pages import DemoPages as de
from selenium.webdriver.support import expected_conditions as EC


class ElementActions:

    def __init__(self, driver):
        self.driver = driver

    def wait(self, seconds):
        time.sleep(seconds)
        logger.info("休息一下")

    def implicitly_wait(self, seconds=5):
        """
        隐式等待--加入默认值，如果没有设置超时时间，则默认等待五秒钟

        :param seconds: 如果没有传入值则默认等待5秒钟
        """
        self.driver.implicitly_wait(seconds)
        logger.info("隐式等待个 %s 秒" % seconds)

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
            self.wait(3)
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

    def target_click(self, x1, y1):  # x1,y1为你编写脚本时适用设备的实际坐标
        # x_1 = x1 / width  # 计算坐标在横坐标上的比例，其中width为传入设备的宽
        # y_1 = y1 / height  # 计算坐标在纵坐标height为传入设备的的高
        self.wait(2)
        size = self.get_size()

        width = size['width']
        height = size['height']



        x_1 = x1 / width  # 计算坐标在横坐标上的比例，其中width为传入设备的宽
        y_1 = y1 / height  # 计算坐标在纵坐标height为传入设备的的高

        # x = self.get_size()['width']  # 获取设备的屏幕宽度
        # y = self.get_size()['height']  # 获取设备屏幕的高度
        self.driver.tap([((x_1 * width, y_1 * height))])
        self.wait(2)

    def wait_ele_visible(self, locator, timeout=20, poll_frequency=0.5):
        """
        :param locator: 查询元素是否可见
        :param timeout:
        :param poll_frequency:
        :return:
        """
        logger.info("等待元素：{} 可见。".format(locator))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            # 输出到日志
            logger.error("查找元素失败！原因是 [%s]" % e.__str__())
            # 失败截取当前页面
            self.save_image_to_allure()
            raise
        else:
            end = time.time()
            logger.info("等待耗时为：{}".format(end - start))

    def wait_contains_element(self, locator, timeout=20, poll_frequency=0.5):
        """
        :param locator:  查询元素是否存在
        :param timeout:
        :param poll_frequency:
        :return:
        """
        logger.info("等待元素：{} 存在。".format(locator))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except Exception as e:
            # 输出到日志
            logger.error("查找元素失败！原因是 [%s]" % e.__str__())
            # 失败截取当前页面
            self.save_image_to_allure()
            raise
        else:
            end = time.time()
            logger.info("等待耗时为：{}".format(end - start))

    def find_element(self, locator, timeout=20, poll_frequency=0.5, wait_exist=False):
        """
        :param locator:
        :param page_action:
        :param timeout:
        :param poll_frequency:
        :param wait: 默认是等待元素可见。
        :return:
        """
        # 先等待元素可见或者存在
        if wait_exist is False:
            self.wait_contains_element(locator)
        else:
            self.wait_ele_visible(locator)
        logger.info("查找元素：{}".format(locator))
        try:
            ele = self.driver.find_element(*locator)
        except Exception as e:
            # 输出到日志
            logger.error("查找元素失败！原因是 [%s]" % e.__str__())
            # 失败截取当前页面
            self.save_image_to_allure()
            raise
        else:
            return ele

    def click(self, locator):
        """
        :param locator:
        :return:
        """
        element = self.driver.find_element(*locator)
        try:
            element.click()
            logger.info("识别元素进行点击操作...")
        except Exception as e:
            logger.error("元素不能识别,原因是: %s" % (e.__str__()))
            self.save_image_to_allure()

    def input(self, locator, text):
        element = self.driver.find_element(*locator)
        try:
            element.send_keys(text)
            logger.info("当前正在进行输入操作:[%s]" % text)
        except Exception as e:
            logger.error("元素不能识别,原因是: %s" % (e.__str__()))
            self.save_image_to_allure()

    def find_elements(self, locator, timeout=20, poll_frequency=0.5, wait_exist=False):
        """
        :param locator:  查找一组元素
        :param locator_timeout: 超时时间
        :return:
        """
        if wait_exist is False:
            self.wait_contains_element(locator)
        else:
            self.wait_ele_visible(locator)
        logger.info("查找元素：{}".format(locator))
        try:
            ele = self.driver.find_elements(*locator)
        except Exception as e:
            # 输出到日志
            logger.error("查找元素失败！原因是 [%s]" % e.__str__())
            # 失败截取当前页面
            self.save_image_to_allure()
            raise
        else:
            return ele

    def select_random_element_content(self, locators):
        """
        :param locators: 随机从列表中获取一个元素进行惦记操作
        :return:
        """
        element_list = self.find_elements(*locators)
        try:
            content_element = []
            for substance in element_list:
                cont = substance.text
                content_element.append(cont)
            content = random.choice(content_element)
            logger.info("获取到的文本信息:%s" % content)
            return content
        except Exception as e:
            logger.error("元素不能识别,原因是: %s" % (e.__str__()))
            self.save_image_to_allure()

    def get_elements_last_content(self, locators):
        """
        :param locators: 获取列表中最后一个元素的文本信息
        :return:
        """
        element_list = self.find_elements(*locators)
        try:
            text = element_list[-1].text
            logger.info("选择列表最后一个元素")
            return text
        except Exception as e:
            logger.error("元素不能识别,原因是: %s" % (e.__str__()))
            self.save_image_to_allure()

    def is_element_exist(self, locator):
        """
        :param locator:  查找元素是否存在
        :return:
        """
        try:
            element = self.find_element(*locator)
            if element:
                logger.info("查找的元素存在")
                return True
            else:
                # 没有发生异常，表示在页面中找到了该元素，返回True
                return True
        except Exception as e:
            logger.error("元素不能识别,原因是: %s" % (e.__str__()))
            self.save_image_to_allure()

    def select_random_element_click_yaml(self, locators):
        """
        :param locators: 随机从列表中获取一个元素进行惦记操作
        :return:
        """
        element_list = self.find_elements_yaml(locators)
        try:
            random_list = []
            for elem in element_list:
                random_list.append(elem)
            random.choice(random_list[:]).click()
        except Exception as e:
            logger.error("[%s] 元素不能识别,原因是: %s" % (locators['element_name'], e.__str__()))
            self.save_image_to_allure()

    def find_element_yaml(self, locator, locator_timeout=5):
        """
        :param locator:  查找单个元素
        :param locator_timeout: 超时时间
        :return:
        """
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
                lambda x: x.find_element(locator_type, locator_value))
            logger.info('[%s] 元素识别成功' % element)
        except Exception as e:
            logger.error("[%s] 元素不能识别,原因是: %s" % (locator['element_name'], e.__str__()))
            self.save_image_to_allure()
        return element

    def find_elements_yaml(self, locator, locator_timeout=5):
        """
        :param locator:  查找一组元素
        :param locator_timeout: 超时时间
        :return:
        """
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
            logger.error("[%s] 元素不能识别,原因是: %s" % (locator['element_name'], e.__str__()))
            self.save_image_to_allure()
        return element

    def select_random_element_content_yaml(self, locators):
        """
        :param locators: 随机从列表中获取一个元素进行惦记操作
        :return:
        """
        element_list = self.find_elements_yaml(locators)
        try:
            content_element = []
            for substance in element_list:
                cont = substance.text
                content_element.append(cont)
            content = random.choice(content_element)
            logger.info("获取到的文本信息:%s" % content)
            return content
        except Exception as e:
            logger.error("[%s] 元素不能识别,原因是: %s" % (locators['element_name'], e.__str__()))
            self.save_image_to_allure()

    def get_elements_last_content_yaml(self, locators):
        """
        :param locators: 获取列表中最后一个元素的文本信息
        :return:
        """
        element_list = self.find_elements_yaml(locators)
        try:
            text = element_list[-1].text
            logger.info("选择列表最后一个元素")
            return text
        except Exception as e:
            logger.error("[%s]元素不能识别,原因是: %s" % (locators['element_name'], e.__str__()))
            self.save_image_to_allure()

    def click_yaml(self, locator):
        """
        :param locator: 从字典中取值
        :return:
        """
        element = self.driver.find_element(locator['locator_type'], locator['locator_value'])
        try:
            element.click()
            logger.info("识别元素进行点击操作...")
        except Exception as e:
            logger.error("[%s] 元素不能识别,原因是: %s" % (locator['element_name'], e.__str__()))
            self.save_image_to_allure()

    def input_yaml(self, locator, text):
        element = self.driver.find_element(locator['locator_type'], locator['locator_value'])
        try:
            element.send_keys(text)
            logger.info("当前正在进行输入操作:[%s]" % text)
        except Exception as e:
            logger.error("[%s] 元素不能识别,原因是: %s" % (locator['element_name'], e.__str__()))
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
