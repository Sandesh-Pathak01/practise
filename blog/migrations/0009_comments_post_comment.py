# Generated by Django 4.2.7 on 2023-12-15 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.posts'),
        ),
    ]
