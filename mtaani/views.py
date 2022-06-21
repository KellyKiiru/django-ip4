
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
    all_hoods = all_hoods[::-1]
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

@login_required
def join_hood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.profile_neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')

@login_required
def leave_hood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.profile_neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')

@login_required
def hood_members(request, post_neighbourhood_id):
    hood = Neighbourhood.objects.get(id=post_neighbourhood_id)
    members = Profile.objects.filter(profile_neighbourhood=hood)
    return render(request, 'all-pages/members.html', {'members': members})

def single_hood(request, post_neighbourhood_id):
    hood = Neighbourhood.objects.get(id=post_neighbourhood_id)
    business = Business.objects.filter(business_neighbourhood=hood)
    posts = Post.objects.filter(post_neighbourhood = hood)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            bsn_form = form.save(commit=False)
            bsn_form.business_neighbourhood = hood
            bsn_form.business_user = request.user.profile
            bsn_form.save()
            return redirect('single-hood', hood.id)
    else:
        form = BusinessForm()
    context = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts,
    }
    return render(request, 'all-pages/single-hood.html', context)

def create_post(request, post_neighbourhood_id):
    hood = Neighbourhood.objects.get(id=post_neighbourhood_id)
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.post_neighbourhood = hood
            new_post.post_user = request.user.profile
            new_post.save()
            return redirect('single-hood', hood.id)
    else:
        form = NewPostForm()
    return render(request, 'all-pages/post.html', {'form': form})

def search_business(request):
    if request.method == 'GET':
        business_name = request.GET.get('post_title')
        results = Business.objects.filter(business_name__icontains=business_name).all()
        display_message = f'business_name'
        
        context = {
            'results': results,
            'display_message': display_message
        }
        return render (request, 'all-pages/search-results.html', context)
    else:
        display_message = " You have not searched for any business"
    return render (request,'all-pages/search-results.html')

def search_all_business(request):
    if request.method == 'GET':
        business_name = request.GET.get('title')
        results = Business.objects.filter(business_name__icontains=business_name).all()
        display_message = f'business_name'
        
        context = {
            'results': results,
            'display_message': display_message
        }
        return render (request, 'all-pages/search-results.html', context)
    else:
        display_message = " You have not searched for any business"
    return render (request,'all-pages/search-results.html')