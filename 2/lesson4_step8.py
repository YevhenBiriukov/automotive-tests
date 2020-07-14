from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    our_price = WebDriverWait(browser, 50).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_value = x_element.text
    y = calc(x_value)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()
    
finally:
    time.sleep(20)
    browser.quit()