from django.shortcuts import render, redirect
from Project.forms import ProjectAddForm
from django.contrib import messages
# Create your views here.
def add_project(request):
    project_add_form = ProjectAddForm()
    context = {"ProjectAddForm": project_add_form, "title": "Add Project"}

    if request.method =="POST":
        project_name= request.POST.get('project_name')
        project_deadlines= request.POSt.get('project_deadlines')
        assigned_hours= request.POst.get('assigned_hours')
        assigned_to= request.POSt.get('assigned_to')
        assigned_date= request.POST.get('assigned_date')
        work_description= request.POST.get("work_description)")

        project_add= ProjectAddForm(request.POST, request.FILES)
        if project_add.is_valid():
            project_add.save()
            messages.success(request, "Project Added Succesfully")
            return redirect("Project")
        return redirect("")

    return render(request, 'project/projects.html')

