# Generated by Django 3.2.9 on 2021-12-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='asd', max_length=100),
            preserve_default=False,
        ),
    ]