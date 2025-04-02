from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
