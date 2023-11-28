from django.db import models
from Employees.models import EmployeeDetail

# Create your models here.
class AssignProject(models.Model):
    project_name = models.CharField(max_length=100)
    project_deadline = models.DateTimeField()
    assigned_hours = models.DecimalField(max_digits=5, decimal_places=2)
    assigned_to = models.ForeignKey(EmployeeDetail, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField()
    work_description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.project_name} - Assigned to: {self.assigned_to.employee_name}"
    
    class Meta:
        db_table = "assign_project"
        ordering = ["-project_name"]