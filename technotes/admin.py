"""Django admoin"""
from django.contrib import admin
from .models import Tech, TechCategory
# Register your models here.

class TechAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug': ["title"]
    }
    list_display = ("title", "category")
admin.site.register(Tech, TechAdmin)
admin.site.register(TechCategory)
