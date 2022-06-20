
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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

@login_required
def profile(request):
    context = {
        "profile": profile,
    }
    if request.user == profile:
        return redirect('profile', context, username=request.user.username)
    return render(request, 'all-pages/profile.html')


@login_required
def edit_profile(request,user_id):
    user=get_object_or_404(User,id=user_id)
    form = UpdateProfileForm()
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            post_profile=form.save(commit=False)
            post_profile.profile_user=user
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm()
    return render(request, 'all-pages/edit_profile.html', {'form': form})

@login_required
def create_new_hood(request):
    #current_user=request.user
    form = NeighbourhoodForm()
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.neighbourhood_admin = request.user
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

@login_required
def add_business(request):
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.business_user = request.user
            business.save()
            return redirect('business')
    else:
        form = BusinessForm()
    return redirect(request,'all-pages/business.html', {"form": form}) 