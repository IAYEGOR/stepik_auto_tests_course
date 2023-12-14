from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")

    for element in elements:

        element.send_keys("Тест")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:

    time.sleep(10)
    browser.close()
    browser.quit()
