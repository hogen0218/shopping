import django_filters
from items_detail.models import Item



class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')   #  此行必须 表示name 使用icontains
    class Meta:
        model = Item
        fields = ['name']