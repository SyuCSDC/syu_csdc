# Generated by Django 5.0.1 on 2024-02-03 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_remove_report_file_reportfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfile',
            name='report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='report.report'),
        ),
    ]