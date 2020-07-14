from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(3)

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_value = x_element.text
    y = calc(x_value)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    time.sleep(20)
    browser.quit()