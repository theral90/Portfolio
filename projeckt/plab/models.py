from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


TARGETS = (
    (1, "samotne_matki"),
    (2, "niepełnosprawni"),
    (3, "dzieci"),
    (4, "osoby_starsze"),
    (5, "bezdomni"),
    (6, "bezrobotni"),
    (7, "wszyscy"),
)

DONATIONS = (
    (1, "zabawki"),
    (2, "książki"),
    (3, "ubrania, które nadają się do ponownego użycia"),
    (4, "ubrania do wyrzucenia"),
    (5, "inne"),
)


class Institutions(models.Model):
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    target = models.IntegerField(choices=TARGETS)
    address = models.CharField(max_length=256)


class Donations(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    donation_type = models.IntegerField(choices=DONATIONS)
    number_of_bags = models.IntegerField(default=0)
    recipient_type = models.IntegerField(choices=TARGETS)
    institution = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    city = models.CharField(max_length=128)
    donation_date = models.DateTimeField(auto_now_add=True)
    pickup_address = models.CharField(max_length=256)
    phone = models.CharField(max_length=128)
    pickup_date = models.DateTimeField()
    transport_notes = models.TextField()
    transfer_status = models.BooleanField(default=False)


"""
class Profile1(models.Model):
    user1 = models.OneToOneField(User, on_delete=models.CASCADE)
    bio1 = models.TextField(max_length=500, blank=True)
    location1 = models.CharField(max_length=30, blank=True)
"""
