from django.db import models

class EmployeeDetail(models.Model):
    employee_id = models.PositiveIntegerField()
    employee_name = models.CharField(max_length=30)
    employee_designation = models.CharField(max_length=50)
    employee_contact = models.CharField(max_length=10)
    
    class Meta:
        db_table = "employee_details"
        ordering = ["employee_name"]

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(EmployeeDetail, on_delete=models.CASCADE)
    date = models.DateField()
    entry_time = models.TimeField()
    exit_time = models.TimeField(null=True, blank=True)
    office_time = models.DurationField()
    break_hour = models.DurationField()

    class Meta:
        db_table = "attendance_records"
        ordering = ["date", "entry_time"]