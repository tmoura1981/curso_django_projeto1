from django.contrib import admin

from .models import Category, Recipe


class RecipeAdmin(admin.ModelAdmin):
    ...


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
