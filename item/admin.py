from django.contrib import admin

# Register your models here.

from .models import Item , ItemImage , Place ,Category , ItemReview ,Itembook
from django_summernote.admin import SummernoteModelAdmin


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Item , SomeModelAdmin)
admin.site.register(ItemImage)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(ItemReview)
admin.site.register(Itembook)


