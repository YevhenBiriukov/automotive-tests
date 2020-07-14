from selenium import webdriver
import time
from selenium.webdriver.common.by import By



try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, "input[required]")
    for element in elements:
       element.send_keys("answer")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()