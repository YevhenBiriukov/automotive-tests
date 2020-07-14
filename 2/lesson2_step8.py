from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("mail@company.com")
    
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    time.sleep(20)
    browser.quit()