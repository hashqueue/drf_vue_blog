from django.db import models
from markdown import Markdown
from django.contrib.auth.models import User
from category.models import Category
from tag.models import Tag
from utils.django_utils.base_model import BaseModel


# Create your models here.

class Article(BaseModel):
    title = models.CharField(max_length=256, help_text='文章标题', verbose_name='文章标题')
    body = models.TextField(help_text='文章正文', verbose_name='文章正文')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='作者ID',
                               related_name='articles')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='分类ID',
                                 related_name='articles')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='文章标签', related_name='articles')

    class Meta:
        db_table = 'article_info'
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        # toc 是渲染后的目录
        return md_body, md.toc
