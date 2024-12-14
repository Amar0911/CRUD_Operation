from django.contrib import admin
from .models import Crud

# Register your models here.

@admin.register(Crud)
class CrudAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']