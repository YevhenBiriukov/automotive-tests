from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img_element = browser.find_element(By.CSS_SELECTOR, "img")
    chest_value = img_element.get_attribute("valuex")
    y = calc(chest_value)

    input_text = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_text.send_keys(y)

    our_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    our_checkbox.click()

    our_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    our_radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()