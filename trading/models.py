from django.db import models

class MemeCoin(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)
    address = models.CharField(max_length=100, unique=True)
    price_usd = models.FloatField()
    liquidity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"
