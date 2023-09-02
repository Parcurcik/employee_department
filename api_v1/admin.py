from django.contrib import admin
from .models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'position', 'department')
    list_filter = ('department', 'position')
    search_fields = ('surname', 'position')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'director')
    search_fields = ('director',)
