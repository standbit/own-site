from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
import unittest
from blog.models import Article
from datetime import datetime


class BasicInstallTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            "/mnt/c/Users/stani/Downloads/chromedriver_win32101022/chromedriver.exe")
        Article.objects.create(
            title="title 1",
            summary="summary 1",
            full_text="full_text 1",
            pubdate=datetime.now(),
            slug="ura"
        )

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # В браузере открывается сайт по ссылке self.live_server_url
        # self.live_server_url = "http://127.0.0.1:8001"
        # Есть заголовок страницы - "Сайт Станислава Яловкина"
        self.browser.get(self.live_server_url)
        self.assertIn("Сайт Станислава Яловкина", self.browser.title)

    def test_home_page_header(self):
        # В шапке сайта написано "Станислав Яловкин"
        self.browser.get(self.live_server_url)
        header = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertIn("Станислав Яловкин", header.text)

    def test_home_page_blog(self):
        # Под шапкой должен быть расположен блог со статьями
        self.browser.get(self.live_server_url)
        article_list = self.browser.find_element(By.CLASS_NAME, "article-list")
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        # У каждой статьи есть заголовок и один абзац с текстом
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(
            By.CLASS_NAME,
            "article-title")
        article_summary = self.browser.find_element(
            By.CLASS_NAME,
            "article-summary")
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    def test_home_page_article_title_link_leads_to_article_page(self):
        # После нажатия пользователем на заголовок статьи на главной странице
        # открывается страница с полным текстом этой статьи 
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(
            By.CLASS_NAME,
            "article-title")
        article_link = article_title.find_element(
            By.TAG_NAME,
            "a")
        article_title_text = article_title.text
        self.browser.get(article_link.get_attribute("href"))
        article_page_title = self.browser.find_element(
            By.CLASS_NAME,
            "article-title")
        self.assertEqual(article_title_text, article_page_title.text)


if __name__ == "__main__":
    unittest.main()
