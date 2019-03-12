from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, default=1, on_delete=models.CASCADE, related_name='employees')
    is_owner = models.BooleanField(default=False)

class Client(models.Model):
    class Meta:
        unique_together = (('company', 'name'),)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clients')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=200)

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)

class Package(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='packages')
    items = models.ManyToManyField('Invoice.Item')
