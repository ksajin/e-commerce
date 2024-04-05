# Generated by Django 5.0.3 on 2024-04-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prd',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prd_name', models.CharField(blank=True, max_length=100, null=True)),
                ('pri', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('prd_pic', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
