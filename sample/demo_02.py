# -*- coding: utf-8 -*-
# @Time : 2021/10/14 16:18
# @Author : Limusen
# @File : demo_01

import os
import yaml

current_path = os.path.dirname(os.path.realpath(__file__))
yml_path = os.path.join(current_path, '..', 'test_data', 'one.yaml')

# def read_yaml(key, yaml_path=yml_path):
#     """
#     读取yaml文件
#     :return: 返回测试数据列表
#     """
#     path = yml_path  # 配置在congfig中的相对路径
#     openYaml = open(path, 'r', encoding='UTF-8')
#     datas = yaml.load(openYaml, Loader=yaml.FullLoader)
#     data = datas[key]
#     print(data)
#
#
# read_yaml(key='app_consulting')


list = {'element_infos': [{'name': 'click_my',
                           'element_info': '//android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView',
                           'find_type': 'xpath', 'operate_type': 'click'},
                          {'name': 'qiyeruzhu', 'element_info': '//android.view.View[@text="企业入驻"]',
                           'find_type': 'xpath', 'operate_type': 'click'},
                          {'name': 'history', 'element_info': '//android.view.View[@text="观看历史"]', 'find_type': 'xpath',
                           'operate_type': 'click'}]}


def demo(text):
    element_infos = {}
    for i in list.values():
        print(i)
        for c in i:
            print(c)
            element_info = {}
            if text == c['name']:
                element_info["locator_name"] = c['name']
                element_info["locator_type"] = c['find_type']
                element_info["locator_value"] = c['element_info']
                element_infos = element_info
        return element_infos


caseData = demo("qiyeruzhu")
print(caseData)
