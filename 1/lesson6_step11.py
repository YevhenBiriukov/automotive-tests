from selenium import webdriver
import time
from selenium.webdriver.common.by import By



try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//label[contains(text(), 'First name*')]/../input")
    input1.send_keys("Juan")
    input2 = browser.find_element(By.XPATH, "//label[contains(text(), 'Last name*')]/../input")
    input2.send_keys("Second")
    input3 = browser.find_element(By.XPATH, "//label[contains(text(), 'Email*')]/../input")
    input3.send_keys("company@company.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
