# -*- coding: utf-8 -*-
# @Time : 2021/10/14 15:59
# @Author : Limusen
# @File : yaml_utils

import os
import yaml
from common.logs_utils import logger

current_path = os.path.dirname(os.path.realpath(__file__))
yml_path = os.path.join(current_path, '..', 'test_data', 'three.yaml')


class YamlUtils:
    def __init__(self):
        pass

    def read_yaml(self, yaml_path=yml_path):
        """
        读取yaml文件
        :return: 返回测试数据列表
        """
        try:
            path = yml_path  # 配置在congfig中的相对路径
            openYaml = open(path, 'r', encoding='UTF-8')
            datas = yaml.load(openYaml, Loader=yaml.FullLoader)
            # data = datas[key]
            # logger.info("读取yml文件中...")
            return datas
        except Exception as e:
            logger.error("未找到文件，请检查对应路径,[%s]" % e.__str__())

    def read_yaml_key(self, key, yaml_path=yml_path):
        """
        读取yaml文件
        :return: 返回测试数据列表
        """
        try:
            path = yml_path  # 配置在congfig中的相对路径
            openYaml = open(path, 'r', encoding='UTF-8')
            datas = yaml.load(openYaml, Loader=yaml.FullLoader)
            data = datas[key]
            logger.info("读取yml文件中...")
            return datas
        except Exception as e:
            logger.error("未找到文件，请检查对应路径,[%s]" % e.__str__())

    def all_data(self):
        data = self.read_yaml()
        return data

    def data_for_key(self, key):
        data = self.read_yaml_key(key)
        return data

    def case_len_key(self, key):
        data = self.read_yaml(key)
        length = len(data['testcase'])
        return length

    def case_len(self, ):
        data = self.read_yaml()
        length = len(data)
        return length

    def get_element_info(self):
        """
        :param i: 读取配置文件中testcase的第几行element_info的值
        :return:
        """
        data = self.all_data()
        return data[0]

    def get_find_type(self, i):
        """
        :param i:  读取配置文件中testcase的第几行find_type的值
        :return:
        """
        data = self.all_data()
        return data['testcase'][i]['find_type']

    def get_one_data(self, text):
        data = self.all_data()
        element_infos = {}
        for c in range(1, len(data[0]['element_infos'])):
            element_info = {}
            if text == data[0]['element_infos'][c]['name']:
                element_info['locator_name'] = data[0]['element_infos'][c]['name']
                element_info["locator_type"] = data[0]['element_infos'][c]['find_type']
                element_info["locator_value"] = data[0]['element_infos'][c]['element_info']
                element_info["element_name"] = data[0]['element_infos'][c]['descprtion']
                # element_infos = data[0]['element_infos'][c]
                element_infos = element_info
        return element_infos

    # def single_data(self, text):
    #     data = self.all_data()
    #     element_infos = {}
    #     for i in range(1, len(data)):
    #         for i in data:
    #             for c in i.keys():
    #                 element_info = {}
    #                 if c == text:
    #                     for c in i.values():
    #                         for value in c:
    #                             # print(value)
    #                             if value['name'] :
    #                                 element_info["name"] = value['name']
    #                                 element_info["locator_type"] = value['find_type']
    #                                 element_info["locator_value"] = value['element_info']
    #                                 element_infos = element_info
    #                         print(element_infos)


if __name__ == '__main__':
    read = YamlUtils()
    print('=====')
    print(read.get_one_data("history"))
    print('=====')
