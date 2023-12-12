# Generated by Django 4.2.7 on 2023-12-06 13:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('post_img', models.ImageField(blank=True, default='default.png', null=True, upload_to='postedpictures', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('profile_pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.profile')),
            ],
        ),
    ]
