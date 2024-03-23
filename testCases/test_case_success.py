# File_name: test_case_success
# Date: 2024-03-18
import pytest
from time import sleep

from configs.allelements import ALLElements
from pageObjects.loginPage import LoginPage
from pageObjects.mainPage import MainPage


@pytest.mark.parametrize('username, password', [('朝天宫002', 123456), ('朝天宫003', 123456)])
def test_login_success_v1(username, password):
    test_loginpage = LoginPage()
    test_loginpage.open_polly_loginpage()
    test_loginpage.login_polly(username, password)
    # sleep(1)
    # test_mainpage = MainPage()
    # assert test_loginpage.get_element_text(test_mainpage['home_page']) == '首页'
    assert test_loginpage.get_element_text(ALLElements.MAINPAGE_LOCATOR) == '首页'
    # 退出
    test_loginpage.click_element(ALLElements.USER_CENTER_LOCATOR)
    sleep(2)
    test_loginpage.click_element(ALLElements.LOGOUT_BUTTON_LOCATOR)
    sleep(2)

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])