from django.contrib import admin
# Register your models here.
from .models import Participant, Profile, ChatRoom, Message, CustomUser

admin.site.register(CustomUser)
admin.site.register(Participant)
admin.site.register(Profile)
admin.site.register(ChatRoom)
admin.site.register(Message)