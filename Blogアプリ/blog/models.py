from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField('', max_length=255)
    created_ad = models.DateTimeField('', default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(
        Category, verbose_name='カテゴリ', on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField('お名前', max_length=30, )
    text = models.TextField('本文')
    post = models.ForeignKey(
        Post, verbose_name='紐づく記事', on_delete=models.PROTECT
    )
    created_at = models.DateTimeField('', default=timezone.now)

    def __str__(self):
        return self.text[:10]