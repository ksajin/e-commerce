# Generated by Django 5.0.3 on 2024-04-05 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_pri_prd_prd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prd',
            old_name='prd',
            new_name='price',
        ),
    ]
