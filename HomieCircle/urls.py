from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post', views.create_post, name='create_post'),

    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('signup', views.signupView, name='register'),

    path('delete_post/<int:postID>', views.deletePost, name='deletePost'),
    path('like_post/<int:postID>', views.like_post, name='like_post'),
    path('dislike_post/<int:postID>', views.dislike_post, name='dislike_post'),
    path('view_post/<int:postID>', views.view_post, name="post"),

    path('account/user/<int:userID>', views.accountSettings, name='account'),
    path('user/<int:userID>', views.userView, name='userView')
]