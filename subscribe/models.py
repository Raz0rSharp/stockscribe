from django.db import models

# Create your models here.
class Subscription(models.Model):
    ticker = models.TextField(max_length=6)
    email = models.EmailField(max_length=254, default="nick.lesho@gmail.com")
    #price = models.DecimalField(max_digits=10, decimal_places=2)
