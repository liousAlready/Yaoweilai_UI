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


list = [{'title': '流程成功', 'desciption': '登录账号并发布资讯', 'caseDatas': {
    'my_btn': ['xpath', '//android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView'],
    'business_position': ['xpath', '//android.view.View[@text="企业入驻"]'],
    'history_look': ['xpath', '//android.view.View[@text="观看历史"]'],
    'information_articles': ['xpath', '//android.view.View[@text="资讯文章"]'], 'input_information_title': ['xpath',
                                                                                                        '//android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText'],
    'click_information_content': ['xpath',
                                  '//android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[@index="0"]'],
    'next_step': ['xpath', '//android.view.View[@text="下一步"]'],
    'article_tag': ['xpath', '//android.view.View[@text="文章标签"]'],
    'select_tag': ['xpath', '//android.view.View[4]/android.view.View[1]/android.view.View[4]'],
    'complete': ['xpath', '//android.view.View[@text="完成"]'], 'release': ['xpath', '//android.view.View[@text="发布"]'],
    'works': ['xpath', '//android.view.View[@text="作品"]']}}]

def demo():
    elements = {}
    for i in list:
        element = {}
        element['case_title'] = i['title']
        element['desciption'] = i['desciption']
        element['case_data'] = i['caseDatas']
        if element['case_data']:
            index = len(element['case_data'])
            for case in element['case_data'].items():
                case_locator_value = case[1]
                print(case_locator_value)
                locator_type = case_locator_value[0]
                locator_value = case_locator_value[1]
                print(locator_type)
                print(locator_value)


        elements = element
    return elements


caseData = demo()
print(caseData)
# print(caseData['case_data'].get("my_btn"))






# def demo():
#     elements = {}
#     for i in list:
#         element = {}
#         element['title'] = i['title']
#         element['desciption'] = i['desciption']
#         element['caseDatas'] = i['caseDatas']
#         elements = element
#     return elements
#
#
# caseData = demo()
# print(caseData)
# print(caseData['caseDatas'].get("my_btn"))
#
