# -*- coding: utf-8 -*-
# @Time : 2021/10/14 17:39
# @Author : Limusen
# @File : consulting

from common.old_yaml_utils import YamlUtils
from common.base_page import ElementActions
from common.driver_util import AppiumTest
from test_data.cousulting_test_suite.consulting_data import ConsultingData as csl


class Consulting(ElementActions):

    def __init__(self, driver):
        super().__init__(driver)

    def click_my_btn(self):
        self.wait(6)
        self.click(csl.my_btn)

    def click_information_btn(self):
        self.wait(1)
        self.click(csl.information_btn)

    def click_information_title(self, title):
        self.click(csl.information_title)
        self.wait(1)
        self.keyboard_input(title)

    def click_information_content(self, content):
        self.click(csl.information_content)
        self.wait(1)
        self.keyboard_input(content)

    def click_next_btn(self):
        self.click(csl.next_btn)

    def click_article_tag(self):
        self.wait(2)
        self.click(csl.article_tag)

    def click_tag_btn(self):
        self.wait(2)
        self.click(csl.tag_btn)

    def click_complete_btn(self):
        self.click(csl.complete_btn)

    def click_only_pic_btn(self):
        self.wait(1)
        self.click(csl.only_pic)

    def click_add_pic(self):
        self.wait(1)
        self.click(csl.add_pic)

    def click_camera_btn(self):
        self.wait(1)
        self.click(csl.camera_btn)

    def click_screenshot_btn(self):
        self.wait(1)
        self.click(csl.screenshot_btn)

    def click_release_btn(self):
        self.click(csl.release_btn)


if __name__ == '__main__':
    driver = AppiumTest().get_driver()
