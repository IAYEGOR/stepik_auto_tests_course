from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, ".first_block input[type='text']")
    for element in elements:
        element.send_keys("Тестовые данные")
    
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:

    time.sleep(30)
    browser.close()
    browser.quit()
