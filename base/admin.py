from django.contrib import admin
from django.utils.html import mark_safe
from base.models.item import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height:80px;" />')
        return "-"
    image_tag.short_description = 'Imagem'