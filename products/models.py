from django.db import models

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=123)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=65)
    summary     = models.TextField(default = 'this is cool', null=False)
    agiled    = models.BooleanField(default=True) #null = True, default = True
    subcribed    = models.BooleanField(blank=False, default=True) #null = True, default = True, NULL default value for previous, blank = field is required