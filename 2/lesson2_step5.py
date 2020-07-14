from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text
    y = calc(x)

    input_text = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_text.send_keys(y)

    our_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    our_checkbox.click()

    our_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    our_radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()