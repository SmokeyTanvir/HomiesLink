from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def index(request):
    context = {
        'posts' : Post.objects.all()
    }

    return render(request, 'HomieCircle/index.html', context)

def create_post(request):
    if request.method == 'POST':
        post = request.POST.get("post")
        post_image = request.FILES.get("post_image")

        newPost = Post(author=request.user.profile, post=post, post_image = post_image)

        newPost.save()

        messages.success(request, 'Post created successfully')
        return redirect('index')            
    
    context = {
        'form': postForm()
    }

    return render(request, 'HomieCircle/create_post.html', context)

def signupView(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            user.save()
            messages.success(request, f'account was created successfully for {username}')
            login(request, user)
            return redirect('index')

    form = CreateUserForm()
    context = {
        'form':form
    }
    return render(request, 'HomieCircle/signup.html', context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'HomieCircle/login.html')

def logoutView(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

def deletePost(request, postID):
    post = Post.objects.get(id=postID)

    if post is not None:
        post.delete()   
        return redirect('index')
    
def like_post(request, postID):
    post = Post.objects.get(id=postID)
    post.likes.add(request.user)
    post.save()
    
    return redirect('index')

def dislike_post(request, postID):
    post = Post.objects.get(id=postID)
    post.likes.remove(request.user)
    post.dislikes.add(request.user)
    post.save()

    return redirect('index')

def view_post(request, postID):

    return render(request, 'HomieCircle/layout.html')


def accountSettings(request, userID):
    user = request.user.profile
    form = userForm(instance=user)

    context = {
        'form': form
    }

    return render(request, 'HomieCircle/account_settings.html', context)



def userView(request, userID):
    user = Profile.objects.get(id=userID)

    context = {
        'user': user 
    }
    return render(request, 'HomieCircle/user.html', context )