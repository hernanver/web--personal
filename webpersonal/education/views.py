from django.shortcuts import render
from .models import Project

# Create your views here.
def education(request):
    projects = Project.objects.all()
    return render(request, "education/education.html", {'projects':projects})
    