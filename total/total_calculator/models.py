from django.db import models

# Create your models here.
class Numbers(models.Model):
     numbers_to_add=list(range(10000001))