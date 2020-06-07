from django.db import models
from django.contrib.auth.models import User as AuthUser
# Create your models here.
class TodoUser(models.Model):
    pass
class TodoItem(models.Model):
    text = models.TextField(default='')
    user = models.ForeignKey(TodoUser,on_delete=models.CASCADE,default=None)

class Profile(models.Model):
    image = models.ImageField(blank=True,upload_to='bio_pics')
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
