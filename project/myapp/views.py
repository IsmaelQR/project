from django.shortcuts import render
from django.http import HttpResponse
from .forms import loginForm,projectForm
from django.shortcuts import redirect
from .models import Project
from django.views.generic.list import ListView

# Create your views here.
def index(request):
    return render(request, "base.html", )

def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            request.session["user"] = str(form.cleaned_data["user"])
            usuario = request.session["user"]
            contra=str(form.cleaned_data["password"])
            #request.session['hora_entrada'] = str(form.cleaned_data["hora_entrada"])
            return redirect("newproject")
    context = {}
    context['form']= loginForm()
    return render(request, "login.html",context)

def newproject(request):
    if request.method == "POST":
        form = projectForm(request.POST)
        if form.is_valid():
            #request.session["user"] = str(form.cleaned_data["user"])
            #usuario = request.session["user"]
            #contra=str(form.cleaned_data["password"])
            #request.session['hora_entrada'] = str(form.cleaned_data["hora_entrada"])
            return redirect("projects")
    context = {}
    context['form']= projectForm()
    return render(request, "newproject.html",context)


def coding(request):
    return render(request, "coding.html")

def home(request):
    return render(request, "home.html", )

def projects(request):
    modeel = projects
    return render(request, "projects.html", )

class proyectList(ListView):
    model = Project
    template_name = "projects.html"