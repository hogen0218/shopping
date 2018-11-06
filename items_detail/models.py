from django.db import models

# Create your models here.
class Gender(models.Model):
    """创建gender分类"""
    name = models.CharField(max_length=20, unique=True, verbose_name='性别分类')

    class Meta:
        verbose_name = '性别分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.name)


class Type(models.Model):
    """创建type分类"""
    name = models.CharField(max_length=20, unique=True, verbose_name='类型分类')

    class Meta:
        verbose_name = '类型分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.name)

class Featured(models.Model):
    """创建featured分类"""
    name = models.CharField(max_length=20, unique=True, verbose_name='货源分类')

    class Meta:
        verbose_name = '货源分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.name)

class Item(models.Model):
    """创建商品数据"""
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='产品名称')
    delivery_time = models.CharField(max_length=20, default='3天', verbose_name='送货时间')
    price = models.FloatField(max_length=20, verbose_name='商品价格')
    ends_time = models.DateTimeField(verbose_name='下架时间')
    desc = models.CharField(max_length=1024, default='本商品占无简介', verbose_name='商品简介')
    color = models.CharField(max_length=10, default='黑色', verbose_name='颜色')
    images = models.ImageField(null=True)
    gender = models.ManyToManyField(Gender)
    type = models.ManyToManyField(Type)
    featured = models.ManyToManyField(Featured)
    # tail = models.FileField(upload_to="vedio", null=True)
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.name)