# File_name: test_login_fail
# Date: 2024-03-20
import os
from time import sleep

import pytest
import allure

from configs.allelements import ALLElements
from configs.config import Config
from pageObjects.loginPage import LoginPage
from utils.handle_path import PollyPath
from utils.tools import get_yaml_data

all_datas = get_yaml_data(PollyPath.data_path / 'login_all_data_title.yaml')
@allure.epic('项目名称：宝利商城自动化测试')
@allure.feature('模块名称：用户登录模块')
@allure.story('用例名称：登录用例')
@pytest.mark.parametrize('title, username, password, msg_locator, msg', all_datas)
# @allure.title('{title}')  # title方法一
@allure.severity('minor')
def test_all_v1(title, username, password, msg_locator, msg):
    allure.dynamic.title(title)  # title方法二
    # allure.dynamic.severity('minor')
    with allure.step('1.打开网页'):
        test_loginpage = LoginPage()
    with allure.step('2.打开宝利商城'):
        test_loginpage.open_polly_loginpage()
    with allure.step('3.登录宝利商城'):
        test_loginpage.login_polly(username, password)
        sleep(3)
    with allure.step('4.断言'):
        with pytest.assume:assert test_loginpage.get_element_text(msg_locator) == msg
    with allure.step('5.断言后的处理，退出'):
        if test_loginpage.driver.current_url == Config.MAINPAGE_URL:
            # 退出
            test_loginpage.click_element(ALLElements.USER_CENTER_LOCATOR)
            sleep(2)
            test_loginpage.click_element(ALLElements.LOGOUT_BUTTON_LOCATOR)
            sleep(2)

if __name__ == '__main__':
    pytest.main([__file__, '-sv', '--alluredir', PollyPath.reports_path, '--clean-alluredir', '--allure-severities=minor'])
    os.system(f'allure serve {PollyPath.reports_path}')