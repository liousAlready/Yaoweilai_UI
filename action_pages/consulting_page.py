# -*- coding: utf-8 -*-
# @Time : 2021/10/14 17:39
# @Author : Limusen
# @File : consulting

import pytest
from common.base_page import ElementActions
from common.driver_util import AppiumTest
from elememt_info_datas.consulting_sutie.consulting_page import Consulting


class ActionConsulting(ElementActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.consult = Consulting(driver)

    def create_information(self, **kwargs):
        self.consult.click_my_btn()
        self.consult.swipe_to_up()
        self.consult.click_information_btn()
        self.consult.click_information_title(kwargs['title'])
        self.consult.click_information_content(kwargs['content'])
        self.consult.click_next_btn()
        self.consult.click_only_pic_btn()
        self.consult.click_add_pic()
        self.consult.click_camera_btn()
        self.consult.click_screenshot_btn()
        self.consult.target_click(kwargs["x1"],kwargs["y1"])
        self.consult.target_click(kwargs["x2"],kwargs["y2"])
        self.consult.wait(3)
        self.consult.click_article_tag()
        self.consult.click_tag_btn()
        self.consult.click_complete_btn()
        self.consult.click_release_btn()


if __name__ == '__main__':
    pass
