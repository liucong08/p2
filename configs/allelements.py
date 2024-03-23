# File_name: allelements
# Date: 2024-03-18
class ALLElements:
    # LoginPage
    USERNAME_LOCATOR = 'id', 'username'
    PASSWORD_LOCATOR = ['id', 'password']
    LOGIN_BUTTON_LOCATOR = 'id', 'btnLogin'
    # MainPage
    MAINPAGE_LOCATOR = 'css selector', '.no-redirect'
    USER_CENTER_LOCATOR = 'css selector', '.user-avatar'
    LOGOUT_BUTTON_LOCATOR= 'xpath', '//span[text()="退出"]'