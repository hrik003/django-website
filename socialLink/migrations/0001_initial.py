# Generated by Django 4.2 on 2023-05-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_name', models.CharField(max_length=255)),
                ('sl_url', models.CharField(max_length=255)),
                ('sl_icon', models.CharField(max_length=255)),
            ],
        ),
    ]
