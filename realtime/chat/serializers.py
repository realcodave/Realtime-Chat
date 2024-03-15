from rest_framework import serializers
from .models import Participant, Profile, ChatRoom, Message


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'
        
    
class MessageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Message
        fields = '__all__'
        
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'