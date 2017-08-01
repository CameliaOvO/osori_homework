from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    view_count = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey('board.Article', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text