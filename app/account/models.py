from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _  

class Account(AbstractUser):
    username = models.CharField(_("username"), max_length=250)
    email = models.EmailField(_("email address"), unique = True)
    image = models.ImageField(upload_to='accounts', null=True)
   

  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]


    class  Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    def __str__(self):
        return  f"Account: {self.email}"