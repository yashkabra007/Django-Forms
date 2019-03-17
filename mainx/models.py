from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    gender = models.CharField(max_length=20)


class ContactForm(models.Model):
    name = models.CharField(max_length=60, blank=False)
    email = models.EmailField(max_length=60, blank=False)
    subject = models.CharField(max_length=128, blank=False)
    message = models.TextField(max_length=500, blank=False)


# Changing User Model in Mid-Project:-
# https://ruddra.com/posts/django-custom-user-migration-mid-phase-project/

