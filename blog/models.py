from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    full_text = models.TextField()
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    pubdate = models.DateTimeField()
    slug = models.CharField(max_length=150, unique=True)
    # is_published = models.BooleanField() # todo

    def __str__(self) -> str:
        return self.title
