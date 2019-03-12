from django.db import models

# Create your models here.

class Item(models.Model):
    product = models.ForeignKey('Company.Product', on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(default=1)

class Quote(models.Model):
    items = models.ManyToManyField(Item)
    url = models.URLField(blank=True, null=True)
    is_accepted = models.BooleanField(default=False)

class PaymnetPeriod(models.Model):
    time_period = models.DurationField()

class Subscription(models.Model):
    package = models.ForeignKey('Company.Package', on_delete=models.CASCADE, related_name='subscriptions')
    date_started = models.DateTimeField(auto_now=True)
    payment_period = models.ForeignKey(PaymnetPeriod, on_delete=models.CASCADE, related_name='subscriptions')

class Payment(models.Model):
    client = models.ForeignKey('Company.Client', on_delete=models.CASCADE, related_name='payments')
    amount = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
