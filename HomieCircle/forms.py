from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username here',
        'class': 'form-control'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'form-control'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'form-control'
    }))


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author', 'likes', 'dislikes']

    post_title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Enter a title for your post", 
        'class': 'form-control'
    }))

    post = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "What's on your mind?",
        'class': 'form-control'
    }))

    post_image = forms.FileField(required=False,widget=forms.ClearableFileInput(attrs={
        'class': 'form-control-file'
    }))

    

class userForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'