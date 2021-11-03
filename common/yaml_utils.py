# -*- coding: utf-8 -*-
# @Time : 2021/11/3 15:58
# @Author : Limusen
# @File : yaml_utils

import yaml
import os
from common.logs_utils import logger

current_path = os.path.dirname(os.path.abspath(__file__))
yaml_path = os.path.join(current_path, '../test_data/demo1.yaml')


class YamlUtils():

    def __init__(self, file_path=yaml_path):
        self.file_path = file_path

    def read_yaml(self):
        """
        读取yaml文件中的某个key的值
        :param key:
        :return:
        """
        try:
            if os.path.exists(self.file_path):
                if self.file_path.endswith('.yaml'):
                    with open(self.file_path, 'r', encoding="utf-8") as e:
                        yaml_info = yaml.load(e.read(), Loader=yaml.FullLoader)
                    value = yaml_info
                    logger.info('读取数据成功...')
                    return value
        except Exception as e:
            logger.error("当前操作报错,原因是: [%s]" % e)

    def read_for_key(self, key):
        """
        根据指定的key读取数据
        :param key: 键的名字
        :return:
        """
        all_data = self.read_yaml()
        try:
            for a in range(1, len(all_data)):
                for i in all_data.items():
                    if i[0] == key:
                        return i[a]
        except Exception as e:
            logger.error("当前操作报错,原因是: [%s]" % e)

    def write_yaml(self, data, encoding='utf-8'):
        '''向yaml文件写入数据'''
        with open(self.file_path, encoding=encoding, mode='w') as f:
            return yaml.dump(data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    # =========== 写入文件 ============
    # data = {
    #     "user": {
    #         "username": "op",
    #         "password": "123456"
    #     }
    # }
    # '''将data数据写入yaml'''
    # write_data = YamlUtils(r"C:\Users\admin\PycharmProjects\Yaoweilai_UI\test_data\demo1.yaml").write_yaml(data)
    # print(write_data)
    # =========== 写入文件 ============

    # =========== 读取文件 ============
    demo = YamlUtils()
    info_data = demo.read_yaml()
    print(info_data)

    # =========== 读取文件 ============
