# Generated by Django 3.1.2 on 2021-08-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arsip', '0006_auto_20210807_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sop',
            name='dokumen',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]