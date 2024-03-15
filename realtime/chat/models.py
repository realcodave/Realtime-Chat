from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profilePics/', null=True, blank=True)
    bio = models.CharField(max_length = 100, default='', blank=True)

class ChatRoom(models.Model):
    
    CHAT_TYPES = [
        ('S', 'Single'),
        ('G', 'Group'),
    ]
    name = models.CharField(max_length = 255, blank=True)
    type = models.CharField(max_length=1, choices=CHAT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
class Participant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    

