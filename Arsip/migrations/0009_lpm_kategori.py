# Generated by Django 3.1.2 on 2021-08-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arsip', '0008_auto_20210807_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='lpm',
            name='kategori',
            field=models.CharField(blank=True, choices=[('UNUJA', 'UNUJA'), ('FAKULTAS', 'FAKULTAS'), ('LEMBAGA', 'LEMBAGA')], max_length=20, null=True),
        ),
    ]
