
from django.shortcuts import render, redirect
from django.http import HttpResponse

from mtaani.models import *
from .forms import *

# Create your views here.

def homepage(request):
    title =  "homepage"
    posts = Post.objects.all()
    neighbourhoods = Neighbourhood.objects.all()
    profiles = Profile.objects.all()
    context = {
        "title": title,
        "profiles": profiles,
        "neighbourhoods": neighbourhoods,
        "posts":posts,
    }
    return render(request, 'all-pages/homepage.html',context)


def profile(request,username):
    
    return render(request, 'all-pages/profile.html')

def edit_profile(request,username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
