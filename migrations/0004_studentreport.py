# Generated by Django 4.0.8 on 2022-11-04 11:12

import ProcessAdminRestApi.models.fields.XLSX_field
import ProcessAdminRestApi.models.upload_model
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic_app', '0003_exerciseupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentReport',
            fields=[
                ('is_calculated', ProcessAdminRestApi.models.upload_model.IsCalculatedField(default=False)),
                ('calculate', ProcessAdminRestApi.models.upload_model.CalculateField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_report', ProcessAdminRestApi.models.fields.XLSX_field.XLSXField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]