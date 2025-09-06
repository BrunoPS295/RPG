from django.contrib import admin
from django.utils.html import mark_safe
from base.models.item import item

@admin.register(item)
class itemAdmin(admin.ModelAdmin):
    list_display = ('name',)

