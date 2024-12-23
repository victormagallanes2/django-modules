from django.contrib import admin
from .models import Products, Category


class ProductsAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
