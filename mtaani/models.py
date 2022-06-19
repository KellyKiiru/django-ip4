from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=50)
    neighbourhood_location = models.CharField(max_length=60)
    neighbourhood_admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    neighbourhood_hood_logo = models.ImageField(upload_to='images/')
    neighbourhood_description = models.TextField()
    neighbourhood_health_tell = models.IntegerField(null=True, blank=True)
    neighbourhood_police_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.neighbourhood_name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)


class Profile(models.Model):
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=50, blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    profile_email = models.EmailField(blank=True)
    #def save_profile(self):
    #    self.save()
        
    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def __str__(self):
        return f'{self.profile_user.username} - profile'

class Business(models.Model):
    business_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    business_name = models.CharField(max_length=120)
    business_email = models.EmailField(max_length=254)
    business_description = models.TextField(blank=True)
    business_neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')

    def __str__(self):
        return f'{self.business_name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(business_name__icontains=name).all()

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
        return f'{self.post_title}'
