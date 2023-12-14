from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    price = WebDriverWait(browser, 15).until (
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    def calc(x):
        return math.log(abs(12*math.sin(int(x))))
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.close()
    browser.quit()
