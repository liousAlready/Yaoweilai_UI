# -*- coding: utf-8 -*-
# @Time : 2021/10/12 17:39
# @Author : Limusen
# @File : devices_utils


import os
import json
from common.logs_utils import logger
from appium import webdriver

current_path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_path, '..', 'config', 'desire_caps.json')


class AppiumTest:

    def __init__(self):
        with open(json_path, "r") as file:
            self.data = json.load(file)
            desired_caps = {}
            desired_caps['platformName'] = self.data['platformName']
            desired_caps['deviceName'] = self.data['deviceName']
            desired_caps['udid'] = self.data['udid']
            # desired_caps['deviceVersion'] = self.data['deviceVersion']
            desired_caps['noReset'] = self.data['noReset']
            desired_caps['unicodeKeyboard'] = self.data['unicodeKeyboard']
            desired_caps['resetKeyboard'] = self.data['resetKeyboard']
            desired_caps['appPackage'] = self.data['appPackage']
            desired_caps['appActivity'] = self.data['appActivity']
            logger.info('当前正在启动app,请稍后.....')
            self.driver = webdriver.Remote("http://%s:%s/wd/hub" % (self.data['host'], self.data['port']), desired_caps)
            self.driver.implicitly_wait(30)

    def get_driver(self):
        return self.driver


if __name__ == '__main__':
    AppiumTest().get_driver()