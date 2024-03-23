# File_name: test_login_fail
# Date: 2024-03-20
from time import sleep

import pytest

from pageObjects.loginPage import LoginPage
from utils.handle_path import PollyPath
from utils.tools import get_yaml_data

file_datas = get_yaml_data(PollyPath.data_path / 'login_fail_data.yaml')
@pytest.mark.parametrize('username, password, msg_locator, msg', file_datas)
def test_fail_v1(username, password, msg_locator, msg):
    test_loginpage = LoginPage()
    test_loginpage.open_polly_loginpage()
    test_loginpage.login_polly(username, password)
    sleep(3)
    assert test_loginpage.get_element_text(msg_locator) == msg

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])