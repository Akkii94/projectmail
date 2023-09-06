from django.db import models

# Create your models here.
event_choice = (
    ('Birthday','Birthday'),
    ('Work Anniversaries','Work Anniversaries.')
)


class Details(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=50)
    event_type = models.CharField(max_length=50, choices=event_choice)
    event_date = models.DateField()



class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    email_id = models.EmailField()




