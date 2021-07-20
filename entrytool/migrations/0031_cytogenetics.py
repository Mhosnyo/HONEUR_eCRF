# Generated by Django 2.0.13 on 2021-06-11 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0040_auto_20201007_1346'),
        ('entrytool', '0030_additionalcharacteristics_qualityoflife5q'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cytogenetics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('cytogenetic_date', models.DateField(verbose_name='Cytogenetic Date')),
                ('del17p', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=25, null=True, verbose_name='del17p')),
                ('ighv_rearrangement', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=25, null=True, verbose_name='IGHV rearrangement')),
                ('del11q', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=25, null=True, verbose_name='del11q')),
                ('tp53_mutation', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=25, null=True, verbose_name='TP53 mutation')),
                ('karyotype', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=25, null=True, verbose_name='Complex Karyotype')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_cytogenetics_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient', verbose_name='Patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_cytogenetics_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Cytogenetic tests',
                'verbose_name_plural': 'Cytogenetic tests',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
