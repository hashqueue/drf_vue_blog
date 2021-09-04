from django.db import models
from utils.django_utils.base_model import BaseModel


# Create your models here.


class Tag(BaseModel):
    name = models.CharField(max_length=128, verbose_name='标签名称')

    class Meta:
        db_table = 'tag_info'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
