from django.db import models


class EmployeeDesignation(models.Model):
    designation_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.designation_name
    
    class Meta:
        db_table = "designation_name"
        ordering = ["-designation_name"]
        
class EmployeeDetail(models.Model):
    
    employee_code = models.PositiveIntegerField(primary_key=True, auto_created=True)
    employee_name = models.CharField(max_length=30)
    employee_designation = models.ForeignKey(EmployeeDesignation, on_delete=models.CASCADE)
    employee_contact = models.CharField(max_length=10)
    employee_image = models.FileField(upload_to="images/employeeImage/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.employee_name} - {self.employee_designation}"
    
    class Meta:
        db_table = "employee_details"
        ordering = ["-employee_name"]

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(EmployeeDetail, on_delete=models.CASCADE)
    date = models.DateField()
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    office_time = models.DurationField()
    break_hour = models.DurationField()

    class Meta:
        db_table = "attendance_records"
        ordering = ["-date", "entry_time"]
        

