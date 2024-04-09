from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products


# admin.site.register(Categories)

admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}