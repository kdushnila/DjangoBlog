import datetime

from django.db import models
from django.db.models import Model
from django.utils import timezone


class Article(Model):
    article_title = models.CharField("Название статьи", max_length=200)
    article_text = models.TextField("Текст статьи")
    pub_date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.CharField("Автор комментария", max_length=50)
    comment_text = models.CharField("Текст комментария", max_length=300)

    def __str__(self):
        return self.comment_author

