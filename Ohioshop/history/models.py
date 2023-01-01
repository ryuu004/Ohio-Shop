from django.db import models

# Create your models here.
class Sells(models.Model):
	fullname = models.CharField(blank=True, max_length=120)
	email = models.EmailField(max_length=254, null=True)
	item = models.TextField(blank=True, null=True)
	quantity = models.DecimalField(decimal_places=2, max_digits=10000) 