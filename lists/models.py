from django.db import models
from django.contrib.auth.models import User as AuthUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.
class TodoUser(models.Model):
    pass


class TodoItem(models.Model):
    text = models.TextField(default='')
    user = models.ForeignKey(TodoUser, on_delete=models.CASCADE, default=None)


class Profile(models.Model):
    image = models.ImageField(default='defaultt.jpg',blank=True, upload_to='bio_pics')
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    def save(self):
        super().save()
        picture = Image.open(self.image.path)
        max_size = (100,100)
        if picture.height > 100 and picture.width > 100:
            picture.thumbnail(max_size)
            picture.save(self.image.path)

    def __str__(self):
        return self.user.username



