from django.db import models
from users.models import User
from items_detail.models import Item
from django.utils.timezone import now



class Comments(models.Model):
    """创建评论数据表"""
    content = models.TextField(null=False, blank=False, verbose_name='评论内容')
    user = models.ForeignKey(User, verbose_name='点评用户')
    item = models.ForeignKey(Item, verbose_name='评论的商品')
    comment_time = models.DateTimeField(default=now, verbose_name='评论时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
