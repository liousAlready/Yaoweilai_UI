"""
======================
Author: 柠檬班-小简
Time: 2020/8/26 21:22
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By

class LoginPageLocs:
    # 用户名输入框
    username_loc = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_loc = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button_loc = (By.TAG_NAME, 'button')
    # 登陆区域的提示框
    error_tips_from_login_area = (By.XPATH, '//div[@class="form-error-info"]')