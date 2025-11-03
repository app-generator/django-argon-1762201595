# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Clinics(models.Model):

    #__Clinics_FIELDS__
    clinicid = models.IntegerField(null=True, blank=True)
    clinicname = models.TextField(max_length=255, null=True, blank=True)

    #__Clinics_FIELDS__END

    class Meta:
        verbose_name        = _("Clinics")
        verbose_name_plural = _("Clinics")


class Providers(models.Model):

    #__Providers_FIELDS__
    providerid = models.IntegerField(null=True, blank=True)
    providername = models.TextField(max_length=255, null=True, blank=True)

    #__Providers_FIELDS__END

    class Meta:
        verbose_name        = _("Providers")
        verbose_name_plural = _("Providers")



#__MODELS__END
