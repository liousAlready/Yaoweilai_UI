# -*- coding: utf-8 -*-
# @Time : 2021/10/20 14:37
# @Author : Limusen
# @File : test_consulting


import pytest
import allure
from common.config_utils import local_config
from action_pages.consulting_page import ActionConsulting


@allure.epic("盛杰-App")
@allure.feature("V1.0")
class TestConsulting:

    @allure.story("资讯发布模块")
    @allure.title("[case01] 发布资讯")
    def test_case_create_information(self, set_up):
        consult = ActionConsulting(set_up)
        consult.create_information(title="发布资讯001", content="发布资讯001", x1=405, y1=393,
                                   x2=870, y2=1953)
        assert 1 == 1

    @allure.story("资讯发布模块")
    @allure.title("[case02] 发布资讯12")
    def test_case_create_information2(self, set_up):
        consult = ActionConsulting(set_up)
        consult.create_information(title="发布资讯0002", content="发布资讯0002", x1=405, y1=393,
                                   x2=870, y2=1953)
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_consulting.py'])
