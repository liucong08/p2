# File_name: test_login_fail
# Date: 2024-03-20
from time import sleep

import pytest

from configs.allelements import ALLElements
from configs.config import Config
from pageObjects.loginPage import LoginPage
from utils.handle_path import PollyPath
from utils.tools import get_yaml_data

all_datas = get_yaml_data(PollyPath.data_path / 'login_all_data.yaml')


@pytest.mark.parametrize('username, password, msg_locator, msg', all_datas)
def test_all_v1(username, password, msg_locator, msg):
    test_loginpage = LoginPage()
    test_loginpage.open_polly_loginpage()
    test_loginpage.login_polly(username, password)
    sleep(3)
    with pytest.assume: assert test_loginpage.get_element_text(msg_locator) == msg
    if test_loginpage.driver.current_url == Config.MAINPAGE_URL:
        # 退出
        test_loginpage.click_element(ALLElements.USER_CENTER_LOCATOR)
        sleep(2)
        test_loginpage.click_element(ALLElements.LOGOUT_BUTTON_LOCATOR)
        sleep(2)


if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
