# -*- coding: utf-8 -*-
# @Time : 2021/10/14 17:39
# @Author : Limusen
# @File : consulting

from common.yaml_utils import YamlUtils
from common.base_page import ElementActions
from common.driver_util import AppiumTest

class Consulting(ElementActions):

    def __init__(self, driver):
        super().__init__(driver)
        elements = YamlUtils().get_yaml(key='app_consulting')
        self.my_btn = elements['caseDatas'].get("my_btn")
        self.business_position = elements['caseDatas'].get("business_position")
        self.history_look = elements['caseDatas'].get("history_look")
        self.information_articles = elements['caseDatas'].get("information_articles")
        self.input_information_title = elements['caseDatas'].get("click_information_content")
        self.next_step = elements['caseDatas'].get("next_step")
        self.article_tag = elements['caseDatas'].get("article_tag")
        self.select_tag = elements['caseDatas'].get("select_tag")
        self.complete = elements['caseDatas'].get("complete")
        self.release = elements['caseDatas'].get("release")
        self.works = elements['caseDatas'].get("works")

    def click_my_btn(self):
        self.wait(1)
        self.click(self.my_btn)

    def print_but(self):
        print(self.my_btn)

if __name__ == '__main__':
    driver = AppiumTest().get_driver()
    Consulting(driver).print_but()
