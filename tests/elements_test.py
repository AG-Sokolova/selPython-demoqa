import time
from pages.base_page import BasePage


class TestElements:

    def test(self, driver):
        page = BasePage(driver, 'https://demoqa.com/text-box')
        page.open()
        time.sleep(5)