# Generated by Django 5.0.1 on 2024-02-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_alter_reportfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfile',
            name='file',
            field=models.FileField(upload_to=' '),
        ),
    ]