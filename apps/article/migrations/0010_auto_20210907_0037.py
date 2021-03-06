# Generated by Django 3.2.7 on 2021-09-07 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
        ('tag', '0002_alter_tag_name'),
        ('article', '0009_rename_tag_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, help_text='作者ID', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='作者ID'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, help_text='分类ID', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='category.category', verbose_name='分类ID'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='文章标签', related_name='articles', to='tag.Tag', verbose_name='文章标签'),
        ),
    ]
