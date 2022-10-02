
from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=100) #it is used for short lenth of string upto 255 char 
    content=models.TextField()  #for more than 255 char
    date_posted=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)#we use one to many relationship coz one user can have multiple post.
    # and we use ondelete=CASCADE if someone delete post it will delete the post


    def __str__(self):
        return self.title #this used just to give name


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
    
