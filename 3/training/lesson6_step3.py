import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.mark.parametrize('correct_url', links)
class TestMainPage1():
    def test_correct_answer(self, browser, correct_url):
        browser.get(correct_url)
        textarea = browser.find_element(By.CSS_SELECTOR, ".textarea")
        our_answer = math.log(int(time.time()))
        textarea.send_keys(str(our_answer))
        button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        button.click()
        time.sleep(1)
        our_element = browser.find_element(By.CSS_SELECTOR, "pre.smart-hints__hint")
        time.sleep(1)
        our_text = our_element.text
        assert our_text == "Correct!", \
            f"the text does not match. Need 'Correct!'. Not {our_text}"