# Generated by Django 2.0 on 2019-03-12 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0004_package_items'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
    ]