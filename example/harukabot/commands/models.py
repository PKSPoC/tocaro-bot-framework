from django.db import models


class Command(models.Model):
    command = models.TextField()
