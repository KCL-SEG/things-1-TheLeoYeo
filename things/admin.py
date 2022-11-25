'''Configuration of administrative interface for hings'''
from django.contrib import admin
from .models import Thing

# Register your models here.
@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    '''Config of the admin interface for users'''
    list_display = ['id',
                    'name',
                    'description',
                    'quantity',
                    'role']