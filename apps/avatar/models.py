from django.db import models
from utils.django_utils.base_model import BaseModel


# Create your models here.


class Avatar(BaseModel):
    url = models.URLField(max_length=256, verbose_name='文章标题背景图URL外链', help_text='文章标题背景图URL外链')

    class Meta:
        db_table = 'avatar_info'
        verbose_name = '文章标题背景图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.url
