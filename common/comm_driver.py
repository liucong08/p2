# File_name: comm_driver
# Date: 2024-03-18
from selenium import webdriver

from configs.config import Config
#单例模式
class Single:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance
class Comm_Driver(Single):
    driver = None
    def get_driver(self, browser_type=Config.BROWSER_TYPE):
        if self.driver is None:
            if browser_type == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser_type == 'firefox':
                self.driver = webdriver.Firefox()

            self.driver.maximize_window()
            self.driver.set_page_load_timeout(Config.SET_PAGE_LOAD_TIMEOUT)

        return self.driver


if __name__ == '__main__':
    s1 = Comm_Driver().get_driver()
    s2 = Comm_Driver().get_driver()
    print(id(s1) == id(s2))