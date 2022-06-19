from .models import *
from django import forms

#class PostForm(forms.ModelForm):
#    class Meta:
#        model = Post
#        fields = ('photo', 'title', 'url', 'description', 'technologies',)
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('profile_user','Neighbourhood')