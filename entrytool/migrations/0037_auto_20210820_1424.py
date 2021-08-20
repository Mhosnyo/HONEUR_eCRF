# Generated by Django 2.0.13 on 2021-08-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0036_auto_20210820_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regimen',
            name='category',
            field=models.CharField(choices=[('Treatment', 'Treatment'), ('Remission', 'Remission'), ('Watch and wait', 'Watch and wait')], max_length=40, verbose_name='Regimen Type'),
        ),
    ]