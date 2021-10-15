# -*- coding: utf-8 -*-
# @Time : 2021/10/12 17:07
# @Author : Limusen
# @File : config_tuils

import configparser
import os

current = os.path.dirname(__file__)
config_path = os.path.join(current, '../config/config.ini')


class ConfigUtils:

    def __init__(self, config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path, encoding="utf-8")

    @property
    def get_consultation_title(self):
        title = self.cfg.get("Consultation", "Consultation_title")
        return title

    @property
    def get_consultation_content(self):
        content = self.cfg.get("Consultation", "Consultation_content")
        return content

    @property
    def log_path(self):
        content = self.cfg.get("logs", "Log_path")
        return content

    @property
    def log_level(self):
        content = self.cfg.get("logs", "Log_level")
        return int(content)

local_config = ConfigUtils()

if __name__ == '__main__':
    print(local_config.log_level)