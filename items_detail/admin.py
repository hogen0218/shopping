from django.contrib import admin
from .models import Item, Gender, Type, Featured


# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    pass
class GenderAdmin(admin.ModelAdmin):
    pass
class TypeAdmin(admin.ModelAdmin):
    pass
class FeaturedAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Featured, FeaturedAdmin)
