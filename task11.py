from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()
        self.browser.quit()

    def perform_registration(self, url):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Тестовые данные")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Тестовые данные")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("Тестовые данные")
        self.browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text

    def test_registration_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.perform_registration(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.perform_registration(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()
