from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Deal(models.Model):
    item_name = models.CharField('Item Name',max_length=100)
    price_buy = models.FloatField('Buy price')
    price_sell = models.FloatField('Sell price')
    deal_status = models.BooleanField('Deal status',max_length=1,default='0')
    date = models.DateField('Deal date',default=timezone.now)
    profit = models.FloatField('Profit',default='0')
    img = models.TextField('item_src',default='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/2048px-No_image_available.svg.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f"Deal{self.item_name}"
    class Meta:
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'

class Profit(models.Model):
    profit = models.FloatField('Profit',default='0')

    def __str__(self):
        return f"Profit{self.profit}"
    class Meta:
        verbose_name = 'Profit'
        verbose_name_plural = 'Profit'