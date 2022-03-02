# -*- coding: utf-8 -*-
# @Time : 2021/10/11 17:37
# @Author : Limusen
# @File : run_all_case

import os
import pytest

current_path = os.path.dirname(os.path.abspath(__file__))
json_report_path = os.path.join(current_path, "report", "json")
html_report_path = os.path.join(current_path, "report", "html")

if __name__ == '__main__':

    pytest.main(['-s', '-v', '--alluredir=%s' % json_report_path, '--clean-alluredir'])
    os.system('allure generate %s -o %s --clean' % (json_report_path, html_report_path))