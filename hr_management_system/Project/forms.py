from django import forms
from Project.models import AssignProject

class ProjectAddForm(forms.ModelForm):
    class Meta:
        
        fields = ("project_name", "project_deadline", "assigned_hours", "assigned_to", "assigned_date", "work_description")
        model= AssignProject