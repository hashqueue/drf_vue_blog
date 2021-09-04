from django.db import models
from utils.django_utils.base_model import BaseModel


# Create your models here.


class Category(BaseModel):
    name = models.CharField(max_length=256, help_text='分类名称', verbose_name='分类名称')

    class Meta:
        db_table = 'category_info'
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
