from email.quoprimime import body_check
from multiprocessing import context
from django.shortcuts import render
from .models import Project, Skill

# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body="")

    skills = Skill.objects.filter(body="")

    context = {"projects": projects, "skills": skills, "detailedSkills": detailedSkills}
    return render(request, "base/home.html", context)
