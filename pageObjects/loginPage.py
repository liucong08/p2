# File_name: loginPage
# Date: 2024-03-18
from common.basePage import BasePage
from configs.allelements import ALLElements
from configs.config import Config


class LoginPage(BasePage):
    '''
    1.打开宝利商城登录页面
    2.login宝利
    '''

    def open_polly_loginpage(self, url=Config.HOST):
        self.open_url(url)

    def login_polly(self, username, password):
        self.input_text(self['username'], username)
        self.input_text(self['password'], password)
        self.click_element(self['login_button'])


if __name__ == '__main__':
    test_loginpage = LoginPage()
    print(test_loginpage.locators)
