# Generated by Django 4.2.7 on 2023-11-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapblog', '0002_web_category_web_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='web',
            name='poster',
            field=models.ImageField(default='images/r5.JPG', upload_to='images/'),
        ),
    ]
