# Generated by Django 4.2.1 on 2023-07-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='category',
            field=models.CharField(default='action', max_length=200),
        ),
    ]