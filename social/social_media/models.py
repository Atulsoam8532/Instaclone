from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
import time


    
class Profile(models.Model):
    
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    follower = models.ManyToManyField(User,blank=True,related_name='follower')
    following = models.ManyToManyField(User,related_name='following',blank=True)
    profile_pic = models.ImageField(upload_to='social_media/pictures/profice/profile_pic')
    Bio = models.CharField(max_length=50,default='Nothing')
    Mobile_number = models.CharField(max_length=20,default='12345678')
    DOB = models.CharField(max_length=20,default='01-01-2000')


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posts = models.ImageField(upload_to='social_media/pictures/profice/post')
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    profiles = models.ForeignKey(Profile,on_delete=models.CASCADE)
    date = models.DateField(default=date.today(),blank=True)
    time = models.TimeField(default=time.strftime("%I:%M:%S"),blank=True)
    saved_user = models.ManyToManyField(User,related_name='saved_user',blank=True)
    def __str__(self):
        return self.user


class Reels(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    reel = models.FileField(upload_to='social_media/pictures/profice/reels')
    likes = models.ManyToManyField(User,related_name='l',blank=True)

class Room(models.Model):
    user_1 = models.ForeignKey(User,on_delete=models.CASCADE)
    user_2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user2')
    is_created = models.BooleanField(default=False)
    room_name = models.CharField(max_length=100,default='Nothing')

class Messeges(models.Model):
    msg = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=datetime.now,blank=True)
    room_id = models.CharField(max_length=100,default='0')


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    comment = models.CharField(max_length=100)
    date_time = models.DateField(default=datetime.now,blank=True)
    likes = models.ManyToManyField(User,related_name='like')

    def __str__(self):
        return self.comment
    



    