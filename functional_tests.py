from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("/mnt/c/Users/stani/Downloads/chromedriver_win32101022/chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # В браузере открывается сайт по ссылке "http://127.0.0.1:8000"
        # Есть заголовок страницы - "Сайт Станислава Яловкина"
        self.browser.get("http://127.0.0.1:8000")
        self.assertIn("Сайт Станислава Яловкина", self.browser.title)

    def test_home_page_header(self):
        # В шапке сайта написано "Станислав Яловкин"
        browser = self.browser.get("http://127.0.0.1:8000")
        header = browser.find_element(By.TAG_NAME, "h1")
        self.assertIn("Станислав Яловкин", header)

if __name__ == "__main__":
    unittest.main()