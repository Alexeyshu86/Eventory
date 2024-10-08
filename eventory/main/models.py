from django.db import models


class Users(models.Model):
    last_name = models.CharField('last_name', max_length=50)
    first_name = models.CharField('first_name', max_length=50)
    phone = models.CharField('phone', max_length=15)
    email = models.CharField('email', max_length=50)
    password = models.CharField('password', max_length=50)

    def __str__(self):
        return self.last_name



