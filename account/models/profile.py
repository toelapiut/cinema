from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..choices import GENDER


# Create your models here.
class Profile(models.Model):
    """
    Current user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(max_length=250, blank=True, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, blank=True, null=True, max_length=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, default=0)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, default=0)
    address = models.CharField(blank=True, null=True, max_length=80)
    postal_code = models.CharField(blank=True, null=True, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        return self.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
