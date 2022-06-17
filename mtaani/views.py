import re
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def homepage(request):
    title =  "homepage"
    context = {
        "title": title,
    }
    return render(request, 'all-pages/homepage.html',context)
