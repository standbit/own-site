from django.urls import resolve
from django.test import TestCase
from blog.views import home_page
from blog.models import Article
from django.http import HttpRequest
from datetime import datetime


class HomePageTest(TestCase):

    def test_home_page_displays_articles(self):
        Article.objects.create(
            title="title1",
            summary="summary1",
            full_text="full_text1",
            pubdate=datetime.now(),
        )
        Article.objects.create(
            title="title2",
            summary="summary2",
            full_text="full_text2",
            pubdate=datetime.now(),
        )
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertIn("title1", html)
        self.assertIn("summary1", html)
        self.assertNotIn("full-text1", html)

        self.assertIn("title2", html)
        self.assertIn("summary2", html)
        self.assertNotIn("full-text2", html)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>Сайт Станислава Яловкина</title>", html)
        self.assertTrue(html.endswith("</html>"))

    def test_home_page_contains_header(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<h1>Станислав Яловкин</h1>", html)
        self.assertTrue(html.endswith("</html>"))


class ArticleModelTest(TestCase):
    def test_article_model_save_and_retrieve(self):
        # создай статью 1
        # сохрани статью 1 в базе
        article1 = Article(
            title="article1",
            full_text="full_text1",
            summary="summary1",
            category="category1",
            pubdate=datetime.now(),
        )
        article1.save()
        # создай статью 2
        # сохрани статью 2 в базе
        article2 = Article(
            title="article2",
            full_text="full_text2",
            summary="summary2",
            category="category2",
            pubdate=datetime.now(),
        )
        article2.save()
        # загрузи из базы все статьи
        all_articles = Article.objects.all()
        # проверь: статьи должно быть две
        self.assertEqual(len(all_articles), 2)
        # проверь что 1 загруженная из базы статья == статья 1
        self.assertEqual(
            all_articles[0].title,
            article1.title
        )
        # проверь что 2 загруженная из базы статья == статья 2
        self.assertEqual(
            all_articles[1].title,
            article2.title
        )
