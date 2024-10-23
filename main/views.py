from django.http import HttpResponse
from django.shortcuts import render


def check_status(request):
    return HttpResponse(status=200)


def index(request):
    return render(request, "index.html")
