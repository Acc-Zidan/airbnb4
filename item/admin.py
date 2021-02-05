from django.contrib import admin

# Register your models here.

from .models import Item , ItemImage , Place ,Category , ItemReview ,Itembook

admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(ItemReview)
admin.site.register(Itembook)


