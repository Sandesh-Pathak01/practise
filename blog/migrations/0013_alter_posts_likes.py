# Generated by Django 4.2.7 on 2023-12-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_posts_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
