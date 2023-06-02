from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True)
    profile_pic = models.ImageField(default="user.png", null=True, blank=True)
    bio = models.CharField(max_length=100)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    author = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    post = models.CharField(max_length=1000)    
    post_image = models.ImageField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_posts', blank=True)

    def __str__(self):
        return f"post {self.id}"
