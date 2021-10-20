# -*- coding: utf-8 -*-
# @Time : 2021/10/20 9:59
# @Author : Limusen
# @File : demo_xx_y

import time
from appium import webdriver

des = {
    "platformName": "Android",
    "platformVersion": "9.0.0",
    "deviceName": "vivo x20",
    "udid": "c6c8c4ce",
    # "appPackage": "com.android.dialer",
    # "appActivity": "com.android.dialer.app.DialtactsActivity",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des)
driver.implicitly_wait(30)
x = driver.get_window_size()
print(x)

width_size = driver.get_window_size()['width']
height_size = driver.get_window_size()['height']

driver.get_screenshot_as_base64()

def get_size():
    size = driver.get_window_size()
    return size

print(get_size())

def target_click(x1, y1):  # x1,y1为你编写脚本时适用设备的实际坐标
    c = driver.get_window_size()
    print(c )
    x_1 = x1 / 1080  # 计算坐标在横坐标上的比例，其中375为iphone6s的宽
    y_1 = y1 / 2034  # 计算坐标在纵坐标667为iphone6s的高
    x = driver.get_window_size()['width']  # 获取设备的屏幕宽度
    y = driver.get_window_size()['height']  # 获取设备屏幕的高度
    print(x_1 * x, y_1 * y)  # 打印出点击的坐标点
    time.sleep(2)
    driver.tap([((x_1 * x, y_1 * y))])
    # wd.tap([(x_1 * x, y_1 * y)], 500)  # 模拟单手点击操作

# 选择图片
target_click(238,1093)


#确定按钮
# target_click(870,1953)

#
# "317 1109  " \
# "1130 1930"
# x = [317, 1109]
# y = [1130, 1930]
# # print(x,y)
#
# w = (y[0] + x[0]) / 2
# h = (y[1] + x[1]) / 2
# print(int(w), int(h))
#
# x0 =  width_size / w
# y0 =  height_size / h
# print(x0,y0)
#
# # print("x0:%.2f, y0: %.2f" % (x0, y0))
#
# new_x = driver.get_window_size()['width']
# new_y = driver.get_window_size()['height']
# print(new_x,new_y)
# print(1.990*new_x,1.837*new_y)
#
# # driver.tap([(1.99*new_x,1.837*new_y)])



