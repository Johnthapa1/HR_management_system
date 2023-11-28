from django import forms
from Project.models import AssignProject

class ProjectAddForm(forms.ModelForm):
    class Meta:
        model= AssignProject 
        fields = ["project_name", "project_deadline", "assigned_hours", "assigned_to", "assigned_date", "work_description"]
        widgets = {
            'project_deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'assigned_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'work_description': forms.Textarea(attrs={'rows': 5, 'cols': 40})
        }