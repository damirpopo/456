from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Stat

def index(request):
    stat = Stat.objects.all()
    return render(request, "index.html", {"stat": stat})

def create(request):
    if request.method == "POST":
        stat = Stat()
        stat.title = request.POST.get("title")
        stat.subtile = request.POST.get("subtile")
        stat.URL = request.POST.get("URL")
        stat.save()
    return HttpResponseRedirect("/")


