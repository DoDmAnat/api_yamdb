# Generated by Django 2.2.16 on 2022-11-05 19:32

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_title_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(default=None, validators=[reviews.models.validate_date], verbose_name='Дата выхода'),
        ),
    ]
