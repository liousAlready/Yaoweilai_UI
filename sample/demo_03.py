# encoding: utf-8
# Author    : limusen
# Datetime  : 2021/10/16 11:05 上午
# User      : lishouwu
# Product   : PyCharm
# Project   : Yaoweilai_UI
# File      : demo_03.py
# explain   : 文件说明


c = {'element_infos': [{'name': 'click_my', 'descprtion': '点击我的',
                        'element_info': '//android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView',
                        'find_type': 'xpath'}, {'name': 'qiyeruzhu', 'descprtion': '点击企业入驻',
                                                'element_info': '//android.view.View[@text="企业入驻"]',
                                                'find_type': 'xpath'},
                       {'name': 'history', 'descprtion': '点击观看历史', 'element_info': '//android.view.View[@text="观看历史"]',
                        'find_type': 'xpath'}]}


print(c.items())
text = "element_infos"
for i in c.keys():
    if text == i :
        print("ss ")