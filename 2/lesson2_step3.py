from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    the_sum1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    the_sum2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    the_sum1_text = the_sum1.text
    the_sum2_text = the_sum2.text
    the_sum = int(the_sum1_text) + int(the_sum2_text)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(the_sum))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()