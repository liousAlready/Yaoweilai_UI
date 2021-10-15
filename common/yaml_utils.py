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

    def get_operate_type(self, i):
        data = self.all_data()
        return data['testcase'][i]['operate_type']

    def single_data(self):
        element_infos = {}
        data = self.all_data()
        print(data)

    def demo_01(self):
        data = self.all_data()
        element_infos = {}
        for da in data:
            element_info = {}
            for i in da.values():
                for c in i:

                    element_info["locator_name"] = c['name']
                    element_info["locator_type"] = c['find_type']
                    element_info["locator_value"] = c['element_info']
                    element_info["element_name"] = c['descprtion']
                    element_infos.update(element_info)
        return element_infos


    # def single_data(self, text):
    #     element_infos = {}
    #     for a in self.all_data().values():
    #         for c in a:
    #             element_info = {}
    #             if text == c['name']:
    #                 element_info["locator_name"] = c['name']
    #                 element_info["locator_type"] = c['find_type']
    #                 element_info["locator_value"] = c['element_info']
    #                 # element_info["element_name"] = c['descprtion']
    #                 element_infos = element_info
    #     return element_infos


if __name__ == '__main__':
    read = YamlUtils()
    print(read.get_element_info())
    print('=====')
    # print(read.all_data())
    print(read.demo_01())
