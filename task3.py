from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, ".form-group #input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    time.sleep(10)
    browser.close()
    browser.quit()
