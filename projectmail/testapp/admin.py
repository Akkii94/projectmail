from django.contrib import admin

from .models import Details, Employee
# Register your models here.


class AdminTable(admin.ModelAdmin):
    list_display = ['employee_id', 'employee_name','event_type', 'event_date']

class AdminEmployee(admin.ModelAdmin):
    list_display = ['emp_id','email_id']

admin.site.register(Details, AdminTable)
admin.site.register(Employee, AdminEmployee)
