# Generated by Django 3.2.7 on 2021-09-03 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '博客文章', 'verbose_name_plural': '博客文章'},
        ),
        migrations.AlterModelTable(
            name='article',
            table='article_info',
        ),
    ]
