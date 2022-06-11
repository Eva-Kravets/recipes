# Generated by Django 4.0.4 on 2022-05-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_calories_carbohydrates_alter_calories_fats_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(to='api.category', verbose_name='Категории'),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='api.ingredient', verbose_name='Ингредиенты'),
        ),
    ]
