from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class profile(models.Model):

    name = models.CharField(max_length=50)
    birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20)
    username = models.OneToOneField(User, on_delete= models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profilepics', default='default.png', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    

    def __str__(self):
        return self.name
    

class posts(models.Model):

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ForeignKey(profile, on_delete= models.CASCADE, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    post_img = models.ImageField(upload_to='postedpictures', default='default.png', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])


class comments(models.Model):

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)

