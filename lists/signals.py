from .models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User as AuthUser
from django.dispatch import receiver

@receiver(post_save,sender=AuthUser)
def create_profile(sender, instance, created, **kwargs):
    print('created',created)
    if created:
        Profile.objects.create(user=instance)
        print('Profile created')

#post_save.connect(create_profile, sender=AuthUser)
