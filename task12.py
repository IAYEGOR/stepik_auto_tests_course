from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

link = "https://stepik.org/lesson/36285/step/1?unit=162401"

try:
    browser = webdriver.Chrome()
    browser.get(link)


finally:
    time.sleep(5)
    browser.close()
    browser.quit()