# Generated by Django 5.0.6 on 2024-07-05 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_delete_courseold'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['start'], 'verbose_name': 'palestra', 'verbose_name_plural': 'palestras'},
        ),
    ]
