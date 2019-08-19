from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
"""

CELE = (
    (1, "samotne_matki"),
    (2, "niepełnosprawni"),
    (3, "dzieci"),
    (4, "osoby_starsze"),
    (5, "bezdomni"),
    (6, "bezrobotni"),
    (7, "wszyscy"),
)

DAROWIZNY = (
    (1, "zabawki"),
    (2, "książki"),
    (3, "ubrania, które nadają się do ponownego użycia"),
    (4, "ubrania do wyrzucenia"),
    (5, "inne"),
)


class Institutions(models.Model):
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    target = models.IntegerField(choices=CELE)
    address = models.CharField(max_length=256)


class UserDonations(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nr_donations = models.IntegerField()
    nr_bags = models.IntegerField()
    nr_institutions = models.IntegerField()


class Donations(models.Model):
    uzytkownik = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    darowizna_type = models.IntegerField(choices=DAROWIZNY)
    worki = models.IntegerField()
    odbiorca_type = models.IntegerField(choices=CELE)
    instytucja = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    miasto = models.CharField(max_length=128)
    darowizna_date = models.DateTimeField(auto_now_add=True)
    adres_odbioru = models.CharField(max_length=256)
    tel = models.CharField(max_length=32)
    data = models.DateField()
    godzina = models.DateTimeField()
    notatka = models.TextField()
    status = models.BooleanField(default=False)
