from django.db import models


class User(models.Model):
    # uid = models.CharField(max_length=10)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    # role = models.CharField(max_length=10)
    fullName = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    # address = models.CharField(max_length=255)
    is_staff = 2
    is_supperuser = 1
    is_active = 1
    # avatar = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_user'