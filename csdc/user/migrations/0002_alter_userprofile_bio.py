# Generated by Django 5.0.1 on 2024-02-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(verbose_name='한 줄 소개'),
        ),
    ]