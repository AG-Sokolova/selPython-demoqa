import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver_manager = ChromeDriverManager().install()
    driver = webdriver.Chrome(driver_manager)
    driver.maximize_window()
    yield driver
    driver.quit()