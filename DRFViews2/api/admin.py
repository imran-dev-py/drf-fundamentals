from django.contrib import admin
from . import models

@admin.register(models.Employee)
class ModelEmployeeAdmin(admin.ModelAdmin):
	list_display = ('name', 'no', 'salary', 'address')
