from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    hood_logo = models.ImageField(upload_to='images/')
    description = models.TextField()
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=50, blank=True, null=True)
    Neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def save_profile(self):
        self.save()
        
    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile
    
    def __str__(self):
        return f'{self.user.username} - Profile'

class Business(models.Model):
    business_name = models.CharField(max_length=120)
    business_email = models.EmailField(max_length=254)
    business_description = models.TextField(blank=True)
    business_neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    business_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

class Post(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posts")
    post_title = models.CharField(max_length=255, blank=True)
    post_description = models.TextField(max_length=255)
    post_profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    post_business = models.ForeignKey(Business, on_delete=models.CASCADE)
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
    
    @classmethod
    def all_posts(cls):
        return cls.objects.all()
    
    
    @classmethod
    def get_profile_image(cls, profile):
        posts = Post.objects.filter(user__pk=profile)
        return posts
        
    def __str__(self):
        return f'{self.title}'
