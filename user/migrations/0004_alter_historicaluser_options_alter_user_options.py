# Generated by Django 4.0.4 on 2022-05-15 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_historicaluser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaluser',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Пользователь', 'verbose_name_plural': 'historical Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
