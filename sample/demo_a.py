# -*- coding: utf-8 -*-
# @Time : 2021/10/27 16:51
# @Author : Limusen
# @File : demo_a

#coding=utf-8
import os

class DosCmd:
    '''
    用来封装windows执行dos命令，分两种，一种是收集执行结果，一种是不需要收集执行结果
    '''
    def excute_cmd_result(self,command):
        '''
        执行command命令，并返回执行结果
        :param command: 传入要执行的命令，字符串格式
        :return:返回执行结果，列表格式
        '''
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))#strip() 方法用于移除字符串头尾指定的字符
        return result_list


    def excute_cmd(self,command):
        '''
        仅执行command命令，不收集执行结果
        :param command: 传入要执行的命令，字符串格式
        '''
        os.system(command)

if __name__=="__main__":
    dos = DosCmd()
    # print(dos.excute_cmd_result('adb devices'))
    dos.excute_cmd('adb devices')