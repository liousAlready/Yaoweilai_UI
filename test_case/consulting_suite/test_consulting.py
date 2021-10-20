# -*- coding: utf-8 -*-
# @Time : 2021/10/20 14:37
# @Author : Limusen
# @File : test_consulting


import pytest
from common.config_utils import local_config
from action_pages.consulting_page import ActionConsulting


class TestConsulting:

    def test_case_create_information(self, set_up):
        driver = set_up
        consult = ActionConsulting(driver)
        consult.create_information(title="hahasd", content="xixixi", x1=405, y1=393,
                                   x2=870, y2=1953)


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
