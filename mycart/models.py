from django.db import models
from items_detail.models import Item
from users.models import User



# Create your models here.


class LineItem(models.Model):
    """购物车数据表"""
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, verbose_name='购物车用户')
    item = models.ForeignKey(Item, verbose_name='购物车用户的商品')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.item.name
