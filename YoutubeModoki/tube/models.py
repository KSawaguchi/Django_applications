from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField('動画タイトル', max_length=255)
    description = models.TextField('説明', blank=True)
    thumbnail = models.ImageField('サムネイル', upload_to='thumbnails/', null=True, blank=True)
    upload = models.FileField('ファイル', upload_to='uploads/%Y/%m/%d/')
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title