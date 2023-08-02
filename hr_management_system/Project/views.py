from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'project/projects.html')

def taskboard(request):
    return render(request, 'project/projects.html')

def tasks(request):
    return render(request, 'project/projects.html')