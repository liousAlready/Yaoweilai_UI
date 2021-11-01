# -*- coding: utf-8 -*-
# @Time : 2021/10/27 17:25
# @Author : Limusen
# @File : devices_utils


import os
from sys import platform as plat


class Devices:

    def excute_cmd(self, command):
        '''
        仅执行command命令，不收集执行结果
        :param command: 传入要执行的命令，字符串格式
        '''
        os.system(command)

    # 　获取已经链接的adb信息
    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    # 检查设备状态
    def attached_devices(self):
        result = self.call_adb("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        flag = [device for device in devices if len(device) > 2]
        if flag:
            return True
        else:
            return False

    # 状态
    def get_state(self):
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None

    # 重启
    def reboot(self, option):
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery"):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    # 将电脑文件拷贝到手机里面
    def push(self, local, remote):
        result = self.call_adb("push %s %s" % (local, remote))
        return result

    # 拉数据到本地
    def pull(self, remote, local):
        result = self.call_adb("pull %s %s" % (remote, local))
        return result

    # 打开指定app
    def open_app(self, packagename, activity):
        result = self.call_adb("shell am start -n %s/%s" % (packagename, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    # 根据包名得到进程id
    def get_app_pid(self, pkg_name):
        if plat == "win32":
            string = self.call_adb("shell ps | findstr " + pkg_name)
            # print(string)
            if string == '':
                return "the process doesn't exist."
            result = string.split(" ")
            # print(result[6])
            return result[6]
        else:
            string = self.call_adb("shell ps | grep " + pkg_name)
            # print(string)
            if string == '':
                return "the process doesn't exist."
            result = string.split(" ")
            # print(result[4])
            return result[4]


if __name__ == '__main__':
    dos = Devices()
    print(dos.attached_devices())
