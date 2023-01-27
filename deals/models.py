from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Deal(models.Model):
    item_name = models.CharField('Item Name',max_length=100, blank=True, null=True)
    price_buy = models.FloatField('Buy price', blank=True, null=True)
    price_sell = models.FloatField('Sell price', blank=True, null=True)
    deal_status = models.BooleanField('Deal status',max_length=1,default='0')
    item_fv =  models.CharField(max_length=32, blank=True, null=True)
    date = models.DateField('Deal date',default=timezone.now)
    profit = models.FloatField('Profit',default='0')
    img = models.TextField('item_src',default='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/2048px-No_image_available.svg.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    view_link = models.TextField('view_link',default='')
    link_status = models.BooleanField('Link status',max_length=1,default='0')
    
    def __str__(self):
        return f"Deal{self.item_name}"
    class Meta:
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'


class Profit(models.Model):
    profit = models.FloatField('Profit',default='0')
    profit_on_sale = models.FloatField('Profit on sale',default='0')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Profit{self.profit}"
    class Meta:
        verbose_name = 'Profit'
        verbose_name_plural = 'Profit'