from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AssignProject(models.Model):
    project_name = models.CharField(max_length=100)
    project_deadline = models.DateTimeField()
    assigned_hours = models.DecimalField(max_digits=5, decimal_places=2)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    work_description = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name
    
    class Meta:
        db_table = "assign_project"
        ordering = ["-project_name"]