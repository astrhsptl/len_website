from django.contrib import admin
from django.contrib.admin import ModelAdmin
from pages.models import News, Products

class ProductsAdmin(ModelAdmin):
    model = Products
    list_display = ['title', 'city', 'is_moderated',]
    list_editable = [ 'is_moderated',]
    fieldsets = (
        (None, {
            'fields': ('title', 'price', 'city', 'user', 'services', 'is_moderated', 'image',)
        }),
    )

admin.site.register(News)
admin.site.register(Products, ProductsAdmin)
