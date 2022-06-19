
from multiprocessing import context
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


def profile(request):
    
    return render(request, 'all-pages/profile.html')

def edit_profile(request,username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm()
    return render(request, 'all-pages/edit_profile.html', {'form': form})


def create_new_hood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourhoodForm()
    return render(request, 'all-pages/new_hood.html', {'form': form})
        
def hoods(request):
    all_hoods = Neighbourhood.objects.all()
    context = {
        'all_hoods': all_hoods,
    }
    return render(request, 'all-pages/all_hoods.html', context)
