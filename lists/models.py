from django.db import models

# Create your models here.
class TodoUser(models.Model):
    pass
class TodoItem(models.Model):
    text = models.TextField(default='')
    user = models.ForeignKey(TodoUser,on_delete=models.CASCADE,default=None)
