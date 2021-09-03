from django.db import models
from django.contrib.auth.models import User
from utils.django_utils.base_model import BaseModel


# Create your models here.

class Article(BaseModel):
    title = models.CharField(max_length=256, help_text='文章标题', verbose_name='文章标题')
    body = models.TextField(help_text='文章正文', verbose_name='文章正文')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者ID', related_name='articles')

    class Meta:
        db_table = 'article_info'
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
