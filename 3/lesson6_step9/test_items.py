import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
]


@pytest.mark.parametrize('correct_url', links)
class TestCommodityPage():
    def test_is_add_to_basket_button_present(self, browser, correct_url):
        browser.get(correct_url)
        button_object = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        time.sleep(5)
        assert button_object, \
            f"there are no 'add to basket' button in this page :("