# File_name: basePage
# Date: 2024-03-18
from common.comm_driver import Comm_Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from configs.config import Config
from utils.handle_path import PollyPath
from utils.tools import get_yaml_data


class BasePage:
    '''
    基类：不同的页面做同样的事
    1.有个页面，输入网址
    2.定位元素
    3.点击事件
    4.输入事件
    5.获取元素的文本（断言）
    '''
    def __init__(self):
        self.driver = Comm_Driver().get_driver()  # alt+enter 获取浏览器对象
        # 得到页面的locator，每个页面获取自己的locator
        self.locators = get_yaml_data(PollyPath.configs_path / 'allelements.yaml')[self.__class__.__name__]
        # 对locator再次拆分，分成name和locator
        for element_name, locator in self.locators.items():
            setattr(self, element_name, locator)

    def open_url(self, url):
        self.driver.get(url)

    def get_element(self, locator, timeout=Config.TIMEOUT, poll_frequency=Config.POLL_FREQUENCY):  # 定位元素
        '''

        :param locator: 元素定位器 类似'id', 'kw'
        :return:
        '''
        return WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))

    def input_text(self, locator, text, append_flag=False):
        '''

        :param locator: 元素定位器 类似'id', 'kw'
        :param text: 要输入的文本
        :param append_flag: 判断是否追加写入
        :return:
        '''
        if append_flag:
            self.get_element(locator).send_keys(text)
        else:
            self.get_element(locator).clear()
            self.get_element(locator).send_keys(text)

    def click_element(self, locator):
        self.get_element(locator).click()

    def get_element_text(self, locator):
        return self.get_element(locator).text

    def __getitem__(self, item):
        return  self.locators[item]
