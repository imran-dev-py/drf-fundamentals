from django.contrib import admin
from . import models

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'no', 'salary', 'address']
