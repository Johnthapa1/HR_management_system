from django.shortcuts import render, redirect
from Project.forms import ProjectAddForm
from django.contrib import messages
from Project.models import AssignProject
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def add_project(request):
    project_add_form = ProjectAddForm()
    context = {"ProjectAddForm": project_add_form, "title": "Add Project"}

    if request.method =="POST":
        project_name= request.POST.get('project_name')
        project_deadlines= request.POST.get('project_deadlines')
        assigned_hours= request.POST.get('assigned_hours')
        assigned_to= request.POST.get('assigned_to')
        assigned_date= request.POST.get('assigned_date')
        work_description= request.POST.get("work_description)")

        project_add= ProjectAddForm(request.POST, request.FILES)
        if project_add.is_valid():
            project_add.save()
            messages.success(request, "Project Added Succesfully")
            return redirect("list_project")
        return redirect("add_project")

    return render(request, 'project/add_project.html', context)

@login_required(login_url='/login/')
def list_project(request):
    list_of_project= AssignProject.objects.all()
    
    paginator = Paginator(list_of_project, 10)  # 10 data in one page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {"page_obj": page_obj}
    return render(request, 'project/list_project.html', context)

