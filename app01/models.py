from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    class Meta:
        db_table = 'user'

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
